variable "TAG" {
  default = "latest"
}
variable "tgt" {
  default = "latest"
}

target "prometheus" {
  dockerfile  = "Dockerfile"
  name = "prometheus-${tgt}"
  context    = "${tgt}"
  tags   = ["10.0.2.6:8083/prometheus:${TAG}-${tgt}"]
}