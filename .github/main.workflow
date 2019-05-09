workflow "Validate configuration" {
  on = "push"
  resolves = ["docker://homeassistant/home-assistant"]
}

action "docker://homeassistant/home-assistant" {
  uses = "docker://homeassistant/home-assistant"
  runs = "hassio "
  args = "ha check"
}
