workflow "Validate configuration" {
  resolves = ["docker://homeassistant/home-assistant:0.92.1"]
  on = "push"
}

action "docker://homeassistant/home-assistant" {
  uses = "docker://homeassistant/home-assistant"
  runs = "./scripts/test.sh"
}
