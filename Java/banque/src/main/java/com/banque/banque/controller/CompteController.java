package com.banque.banque.controller;

import com.banque.banque.model.Compte;
import com.banque.banque.service.CompteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

import java.util.Optional;

@RestController
public class CompteController {
    @Autowired
    private CompteService compteService;

    @GetMapping("/compte/lister")
    public ModelAndView getComptes() {
        return new ModelAndView("listeComptes", "comptes", compteService.getComptes());
    }

    @GetMapping("/compte/lister/{id}")
    public ModelAndView getCompte(@PathVariable("id") final Integer id) {
        Optional<Compte> compte = compteService.getCompte(id);

        return new ModelAndView("detailCompte", "compte", compte.orElse(null));
    }

    @GetMapping("/compte/creer")
    public ModelAndView creerCompte() {
        return new ModelAndView("creerCompte", "compte", new Compte());
    }

    @PostMapping("/compte/creer")
    public ModelAndView submit(@ModelAttribute("compte") Compte compte, ModelMap model) {
        model.addAttribute("numero", compte.getNumero());
        model.addAttribute("client", compte.getClient());

        compteService.saveCompte(compte);

        return getComptes();
    }

    @DeleteMapping("/compte/effacer/{id}")
    public void deleteCompte(@PathVariable("id") final Integer id) {
        compteService.deleteCompte(id);
    }
}
