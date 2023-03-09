package com.example.kolin_feign.GET

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.RestController

@RestController
class PedidoController(private val pedidoClient: PedidoClient) {
    @GetMapping("/pedido/{id}")
    fun getPedido(@PathVariable id: Int): Pedido {
        return pedidoClient.getPedido(id)
    }
}