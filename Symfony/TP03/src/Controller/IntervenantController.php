<?php

namespace App\Controller;

use App\Entity\Intervenant;
use App\Form\IntervenantFormType;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class IntervenantController extends AbstractController
{
    #[Route('/intervenant', name: 'intervenant')]
    public function index(): Response
    {
        $entityManager = $this->getDoctrine()->getManager();

        $inter = new Intervenant();
        $inter->setNom("Dubois");
        $inter->setSpecialiteprofessionnelle("Ingenieur systemes");

        $entityManager->persist($inter);

        $entityManager->flush();

        return new Response("Creation d'un intervevant avec l'id : ". $inter->getId());
    }

    #[Route('/intervenant/create', name: 'intervenant_create')]
    public function new(Request $request)
    {
        $task = new Intervenant();

        $form = $this->createForm(IntervenantFormType::class, $task);

        $form->handleRequest($request);
        if($form->isSubmitted() && $form->isValid()) {
            $task = $form->getData();

            $entityManager = $this->getDoctrine()->getManager();
            $entityManager->persist($task);
            $entityManager->flush();
            return $this->redirectToRoute('newIntervenant_success');
        }

        return $this->render("intervenant/new.html.twig", [
            'intervenantForm' => $form->createView(),
        ]);
    }

    #[Route('/intervenants', name: 'intervenant_liste')]
    public function getIntervenants()
    {
        $inter = $this->getDoctrine()
            ->getRepository(Intervenant::class)
            ->findAll();

        return $this->render("intervenant/liste.html.twig", [
            'intervenants' => $inter
        ]);
    }

    #[Route('/intervenant/{id}', name: 'intervenant_detail')]
    public function show($id)
    {
        $inter = $this->getDoctrine()
            ->getRepository(Intervenant::class)
            ->find($id);

        if(!$inter) {
            throw $this->createNotFoundException("Pas d'intervenant pour cet id : ". $id);
        }

        return new Response(
            "Id : " . $id . " Nom intervenant : " . $inter->getNom()
        );
    }
}
