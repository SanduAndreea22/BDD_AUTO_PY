BDD Automation Framework with Python & Behave
Acest proiect reprezintă un framework de testare automată construit folosind Python și Behave, implementând metodologia BDD (Behavior Driven Development) și design pattern-ul Page Object Model (POM).

🚀 Tehnologii Utilizate
• Limbaj: Python 3.12

• Framework BDD: Behave (Gherkin)

• Automatizare Browser: Selenium WebDriver

• Arhitectură: Page Object Model (POM)

📂 Structura Proiectului
• `features/` - Conține scenariile de testare scrise în format Gherkin (`.feature`).

• `pages/` - Conține clasele de tip Page Object pentru incapsularea selectorilor și a logicii paginilor.

• `steps/` - Implementarea pașilor definiți în fișierele feature.

• `browser.py` - Gestionarea instanței de browser.

• `behave.ini` - Fișierul de configurare pentru Behave.

🛠️ Instalare și Rulare
1. Instalează dependențele necesare:

```

pip install behave selenium

```

2. Execută toate testele:

```

behave

```


📝 Detalii Proiect
Proiectul include teste automate pentru funcționalitățile de Login și Gestiune Cărți, asigurând o acoperire solidă a fluxurilor principale de utilizator.
