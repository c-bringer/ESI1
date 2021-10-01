<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class FrontController extends AbstractController
{
    /**
     * @Route("/")
     */
    public function index()
    {
        return new Response("Bonjour");
    }

    /**
     * @Route("/produits/{var}")
     * @param $var
     */
    public function afficheCreneau($var)
    {
        $commentaires = [
            "Je ne serais pas disponible sur cette période (Gauthier)",
            "Je veux bien assurer la relève (Sophie)",
            "Pensez à reporter l'heure manquante (Mélanie)"
        ];

        return $this->render("affiche.html.twig", [
            'title' => ucwords(str_replace('-', ' ', $var)),
            'commentaires' => $commentaires
        ]);
    }
}