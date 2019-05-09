workflow "Validate configuration" {
  resolves = ["docker://homeassistant/home-assistant"]
  on = "watch"
}

action "docker://homeassistant/home-assistant" {
  uses = "docker://homeassistant/home-assistant"
  runs = "hassio "
  args = "ha check"
}
