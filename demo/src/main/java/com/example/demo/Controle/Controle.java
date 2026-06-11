package com.example.demo.Controle;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import com.example.demo.Modelo.Pessoa;
import com.example.demo.Repositorio.Repositorio;
import org.springframework.beans.factory.annotation.Autowired;



@RestController
public class Controle {
    @Autowired
    private Repositorio acao;
    
    @PostMapping("/api")
    public Pessoa cadastrar(@RequestBody Pessoa pessoa){
        return acao.save(pessoa);
    }

    @GetMapping("/")
    public String hello(){
        return "Hello World";
    }

    @GetMapping("/boasvindas")
    public String boasvindas(){
        return "Seja bem vindo";
    }

    @GetMapping("/boasvindas/{nome}")
    public String boasvindas(@PathVariable String nome){
        return "Seja bem vindo, " + nome;
    }
    @PostMapping("/pessoa")
    public Pessoa pessoa(@RequestBody Pessoa p){
        return p;
    }
}
    

