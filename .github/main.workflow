workflow "Validate configuration" {
  resolves = ["docker://homeassistant/home-assistant"]
  on = "push"
}

action "docker://homeassistant/home-assistant" {
  uses = "docker://homeassistant/home-assistant@0.92.1"
  runs = "./scripts/test.sh"
}
