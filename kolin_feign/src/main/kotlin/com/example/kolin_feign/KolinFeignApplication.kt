package com.example.kolin_feign

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.cloud.openfeign.EnableFeignClients

@SpringBootApplication
@EnableFeignClients
class KolinFeignApplication

fun main(args: Array<String>) {
	runApplication<KolinFeignApplication>(*args)
}
