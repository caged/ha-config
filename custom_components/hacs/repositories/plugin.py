"""Class for plugins in HACS."""
import json
from integrationhelper import Logger

from custom_components.hacs.hacsbase.exceptions import HacsException
from custom_components.hacs.helpers.information import find_file_name
from custom_components.hacs.repositories.repository import HacsRepository


class HacsPlugin(HacsRepository):
    """Plugins in HACS."""

    def __init__(self, full_name):
        """Initialize."""
        super().__init__()
        self.data.full_name = full_name
        self.data.file_name = None
        self.data.category = "plugin"
        self.information.javascript_type = None
        self.content.path.local = self.localpath
        self.logger = Logger(f"hacs.repository.{self.data.category}.{full_name}")

    @property
    def localpath(self):
        """Return localpath."""
        return f"{self.hacs.system.config_path}/www/community/{self.data.full_name.split('/')[-1]}"

    async def validate_repository(self):
        """Validate."""
        # Run common validation steps.
        await self.common_validate()

        # Custom step 1: Validate content.
        find_file_name(self)

        if self.content.path.remote is None:
            raise HacsException(
                f"Repostitory structure for {self.ref.replace('tags/','')} is not compliant"
            )

        if self.content.path.remote == "release":
            self.content.single = True

        # Handle potential errors
        if self.validate.errors:
            for error in self.validate.errors:
                if not self.hacs.system.status.startup:
                    self.logger.error(error)
        return self.validate.success

    async def update_repository(self, ignore_issues=False):
        """Update."""
        await self.common_update(ignore_issues)

        # Get plugin objects.
        find_file_name(self)

        if self.content.path.remote is None:
            self.validate.errors.append(
                f"Repostitory structure for {self.ref.replace('tags/','')} is not compliant"
            )

        if self.content.path.remote == "release":
            self.content.single = True

    async def get_package_content(self):
        """Get package content."""
        try:
            package = await self.repository_object.get_contents("package.json")
            package = json.loads(package.content)

            if package:
                self.data.authors = package["author"]
        except Exception:  # pylint: disable=broad-except
            pass
