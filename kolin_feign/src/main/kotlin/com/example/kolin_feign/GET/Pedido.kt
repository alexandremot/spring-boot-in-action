package com.example.kolin_feign.GET

data class Pedido(
        val atendente: String,
        val id: Int,
        val mesa: String,
        val pedido: String,
        val quantidade: Int,
        val valor: Double
)