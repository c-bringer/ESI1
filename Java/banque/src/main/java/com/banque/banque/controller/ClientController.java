package com.banque.banque.controller;

import com.banque.banque.model.Client;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.*;
import com.banque.banque.service.ClientService;
import org.springframework.web.servlet.ModelAndView;

import java.util.Optional;

@RestController
public class ClientController {
    @Autowired
    private ClientService clientService;

    @GetMapping("/client/lister")
    public ModelAndView getClients() {
        return new ModelAndView("listeClients", "clients", clientService.getClients());
    }

    @GetMapping("/client/lister/{id}")
    public ModelAndView getClient(@PathVariable("id") final Integer id) {
        Optional<Client> client = clientService.getClient(id);

        return new ModelAndView("detailClient", "client", client.orElse(null));
    }

    @GetMapping("/client/creer")
    public ModelAndView creerClient() {
        return new ModelAndView("creerClient", "client", new Client());
    }

    @PostMapping("/client/creer")
    public ModelAndView submit(@ModelAttribute("client") Client client, ModelMap model) {
        model.addAttribute("nom", client.getNom());
        model.addAttribute("prenom", client.getPrenom());

        clientService.saveClient(client);

        return getClients();
    }

    @DeleteMapping("/client/effacer/{id}")
    public void deleteClient(@PathVariable("id") final Integer id) {
        clientService.deleteClient(id);
    }

//            /client/editer	édition d'un client
}
