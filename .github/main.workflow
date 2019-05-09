workflow "Validate configuration" {
  resolves = ["docker://homeassistant/home-assistant"]
  on = "push"
}

action "docker://homeassistant/home-assistant" {
  uses = "docker://homeassistant/home-assistant"
  runs = "python"
  args = "-m homeassistant -c / --script check_config --info all"
}
