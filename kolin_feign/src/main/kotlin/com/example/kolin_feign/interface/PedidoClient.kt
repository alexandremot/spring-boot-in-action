package com.example.kolin_feign.`interface`

import com.example.kolin_feign.data_model.Pedido
import org.springframework.cloud.openfeign.FeignClient
import org.springframework.http.MediaType
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody


@FeignClient(name = "pedidoClient", url = "http://localhost:5000")
interface PedidoClient {
    @GetMapping("/pedido/{id}")
    fun getPedido(@PathVariable id: Int): Pedido

    @PostMapping(path = ["/pedido"], consumes = [MediaType.APPLICATION_JSON_VALUE])
    fun addPedido(@RequestBody pedidoRequest: Pedido): String
}