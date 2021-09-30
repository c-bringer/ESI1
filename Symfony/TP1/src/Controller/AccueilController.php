<?php

namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class AccueilController
{
    /**
     * @return Response
     */
    public function index()
    {
        return new Response("Voici la page principale : Corentin BRINGER");
    }

    /**
     * @Route("/commandes/recapitulatif")
     * @return Response
     */
    public function recapCommandes()
    {
        return new Response("Récapitulatif des commandes");
    }

    /**
     * @Route("/commandes/{statut}")
     * @param $joker
     * @return Response
     */
    public function recapCommandesStatut($statut)
    {
        return new Response(sprintf("Liste des commandes : %s", $statut));
    }
}