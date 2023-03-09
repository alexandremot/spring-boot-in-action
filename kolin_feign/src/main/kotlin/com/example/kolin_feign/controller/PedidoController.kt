package com.example.kolin_feign.controller

import com.example.kolin_feign.`interface`.PedidoClient
import com.example.kolin_feign.data_model.Pedido
import org.springframework.web.bind.annotation.*

@RestController
class PedidoController(private val pedidoClient: PedidoClient) {
    @GetMapping("/pedido/{id}")
    fun getPedido(@PathVariable id: Int): Pedido {
        return pedidoClient.getPedido(id)
    }

    @PostMapping("/pedido")
    fun addPedido(@RequestBody pedidoRequest: Pedido): String {
        return pedidoClient.addPedido(pedidoRequest)
    }
}