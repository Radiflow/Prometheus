variable "TAG" {
  default = "latest"
}
variable "tgt" {
  default = "latest"
}

target "prometheus" {
  dockerfile  = "Dockerfile"
  context    = "conf/${tgt}"
  tags   = ["10.0.2.6:8083/prometheus:${TAG}-${tgt}"]
}