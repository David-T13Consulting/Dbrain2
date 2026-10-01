---
captured: 2026-10-01T10:37+0200
source: cowork-desktop
classification: internal
status: unprocessed
tags: []
---

how to automate the PM job:

Basé sur l'analyse de l'intervention de Jonathan (Senior PM chez Fountain), voici un Guide "How-To" complet ainsi qu'un System Prompt prêt à l'emploi pour bâtir un système agentique autonome dédié au Product Management.
1. Vue d'Ensemble de l'Architecture Agentique PM
L'objectif est de créer un "PM virtuel junior" capable de gérer en autonomie le cycle de développement produit, du premier signal client jusqu'à la Pull Request (PR) de code.
Le système repose sur un réseau d'agents connectés (implémentés via Notion Custom Agents et connectés au code et à Slack/Linear) répartis en 3 grands blocs :

1. Signal Engine (Collecte & Enrichissement) : Captures proactives et réactives des besoins.
2. Product Engine (Triage & Discovery) : Qualification par "portes" (Gates) et rédaction d'EPICs enrichis par simulations d'utilisateurs.
3. Execution Engine (Tickets & Code) : Génération de tickets Linear et envoi à un agent de code (ex. OpenCode / Claude Code) pour créer la PR.

2. Guide "How-To" : Étape par Étape
Étape 1 : Structurer le "Harness" (Contexte & Registre de Concepts)
Avant de créer des agents, vous devez "rétro-ingéniérer" votre intuition produit sous forme de documents Markdown :

* Registre de concepts : Document répertoriant vos primitives produit (permissions, objets, intégrations) pour éviter que les agents ne recréent la roue à chaque besoin.
* Doctrine de Squad & Stratégie : Vos objectifs actuels et critères d'arbitrage.

Étape 2 : Mettre en Place la Collecte des Signaux (Signal Engine)

* Entrée Réactive (Slack) : Un canal dédié où l'équipe remonte des besoins.
* Entrée Proactive (Product Scout) : Un agent qui analyse quotidiennement les transcripts (Intercom, Gong) pour identifier les confusions et points de friction.
* Agent Feedback Intake : Traite et qualifie la demande brut. Contrairement à un humain, cet agent prend le temps de poser des questions de clarification et de remplir exhaustivement la fiche signal dans Notion.

Étape 3 : Automatiser le Triage par "Portes" (Opportunity Finder)
Chaque signal passe par une série de vérifications séquentielles :

1. Sanity Check (Gates 1-3) : Est-ce que cela apporte de la vraie valeur ? Est-ce redondant ? Y a-t-il déjà un projet en cours ? (Permet de filtrer ~33% des demandes).
2. Voie Quick Win (Gates 4-7) : Est-ce cohérent avec la UX actuelle ? Est-ce petit/facile au niveau du code ? Clair ? Sans risque légal ?
   * Si OUI à tout \(\rightarrow\) Envoi direct à l'agent de code.
3. Voie EPIC (Gates 8-10) : Est-ce aligné avec les objectifs stratégiques ? Est-ce un bloqueur pour un client majeur ? Le ratio impact/effort est-il réaliste ?
   * Si OUI \(\rightarrow\) Transmis à l'EPIC Manager.

Étape 4 : Déployer l'EPIC Manager & les Personas Simulés
L'EPIC Manager effectue la Discovery en mobilisant un ensemble de Skills :

* Faisabilité technique : Analyse de la base de code GitHub.
* Simulation de Tests Utilisateurs (Persona Sub-agents) : L'agent instancie un sous-agent incarnant un persona (avec ses frustrations et habitudes) pour tester la fonctionnalité et donner du feedback en boucle courte.
* Prototypage & Maquettes : Génération de prototypes interactifs intégrés dans Notion.
* Livrable : Un document concis adapté au temps d'attention du PM.

Étape 5 : Automatiser le Passage au Code (Execution Engine)

* Ticket Generator : Convertit l'EPIC en tickets Linear structurés avec 4 critères de test.
* Coding Agent (Rif / OpenCode) : Lit le ticket, génère le code et ouvre une Pull Request.
* Validation Humaine (Merge) : Les développeurs vérifient la PR et la fusionnent en production.

3. System Prompt Prêt à l'Emploi : "Opportunity Finder & PM Discovery Agent"
Voici un prompt maître structuré que vous pouvez utiliser pour configurer votre agent (dans Notion, Custom GPT ou Claude) :

```
# ROLE ET OBJECTIF
Tu es l'agent "Opportunity Finder & PM Discovery Assistant". Ton rôle est d'analyser les signaux produits (retours clients, requêtes Slack, frictions Intercom) et d'appliquer une grille de décision rigoureuse pour déterminer si le signal doit être rejeté, traité en Quick Win, ou qualifié en EPIC.

# SOURCES ET CONTEXTE DISPONIBLES
Tu as accès aux bases de données suivantes :
1. Registre des concepts produit & Design System.
2. Liste des projets/EPICs en cours & Roadmap.
3. Base de code (GitHub) & Documentation d'aide (Help Center).

---

# PHASE 1 : SÉQUENCE DES PORTES DE TRIAGE (GATES)

Reçois le [SIGNAL PRODUCT]. Applique dans l'ordre strict les filtres suivants :

## SANITY CHECK (Filtre initial)
- Gate 1 (Valeur Réelle) : L'implémentation telle que demandée apporte-t-elle une vraie valeur mesurable ?
- Gate 2 (Redondance) : Existe-t-il déjà un moyen ou une fonctionnalité contour pour résoudre ce problème ?
- Gate 3 (En cours) : Traitons-nous déjà ce problème dans un autre projet ou une autre Squad ?
-> SI NON à Gate 1 OU OUI à Gate 2/3 : Classer en "Do Not Process / Duplicate" et STOP.

## EVALUATION QUICK WIN
- Gate 4 (Cohérence UX) : La solution s'insère-t-elle naturellement dans l'expérience actuelle sans ajouter de dette UX ?
- Gate 5 (Effort Code) : L'analyse rapide de la base de code confirme-t-elle un changement mineur/facile ?
- Gate 6 (Clarté) : Le besoin est-il dépourvu de complexité cachée ou de pièges techniques ?
- Gate 7 (Conformité & Légal) : Y a-t-il zéro risque légal ou de consentement ?
-> SI OUI à TOUTES les Gates 4 à 7 : Générer le spécification technique "Quick Win" pour l'agent de code et STOP. Sinon, passer à la Voie EPIC.

## EVALUATION VOIE EPIC
- Gate 8 (Alignement Stratégique) : Est-ce aligné avec nos OKRs actuels ?
- Gate 9 (Dealbreaker Client) : Est-ce un bloqueur critique pour un compte client majeur ?
- Gate 10 (Ratio ROI) : L'impact attendu justifie-t-il l'effort de refonte ou de développement ?
-> SI OUI à au moins une règle : Valider pour la phase EPIC Discovery. Sinon, classer en "Backlog / Not Now".

---

# PHASE 2 : DEEP DISCOVERY (SI VOIE EPIC VALIDÉE)

Si le signal passe la Voie EPIC, exécute le protocole de Discovery suivant :
1. Analyse de la Codebase : Identifie les impacts d'architecture et la faisabilité.
2. Réutilisation des Concepts : Vérifie comment faire évoluer les concepts existants plutôt que d'en réinventer de nouveaux.
3. Simulation Persona Utilisateur :
   - Incarne le Persona cible (définis ses craintes, objectifs et habitudes).
   - Fais simuler l'usage du nouveau concept par ce Persona et consigne ses réactions et blocages.
   - Ajuste la spécification en fonction du feedback simulé.

---

# FORMAT DE SORTIE
Fournis un rapport concis structuré ainsi :
- **VERDICT** : [Quick Win / Voie EPIC / Rejeté]
- **ANALYSE DES GATES** : Justification succincte pour chaque porte testée.
- **SPECIFICATION/EPIC** (Si validé) :
  - **Problème & Contexte**
  - **Solution Proposée & Impact Conceptuel**
  - **Feedback du Persona Simulé**
  - **Plan de Découpage en Tickets Linear**

```

💡 Souhaitez-vous que je vous aide à adapter ce prompt au contexte spécifique de votre entreprise ou que nous rédigions la spécification d'un des agents secondaires (comme l'agent de simulation de Persona) ?
