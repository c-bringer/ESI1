package com.banque.banque.model;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "compte")
public class Compte
{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "numero", length = 50)
    private String numero;

    @ManyToOne
    @JoinColumn(name = "idClient")
    private Client client;
}
