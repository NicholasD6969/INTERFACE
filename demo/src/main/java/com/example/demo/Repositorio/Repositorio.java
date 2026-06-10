package com.example.demo.Repositorio;

import org.springframework.data.repository.CrudRepository;
import com.example.demo.Modelo.Pessoa;

public interface Repositorio extends CrudRepository<Pessoa, Integer> {
}
