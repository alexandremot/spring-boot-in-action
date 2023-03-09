package com.example.kolin_feign.GET

import org.springframework.cloud.openfeign.FeignClient
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable


@FeignClient(name = "pedidoClient", url = "http://localhost:5000")
interface PedidoClient {
    @GetMapping("/pedido/{id}")
    fun getPedido(@PathVariable id: Int): Pedido
}