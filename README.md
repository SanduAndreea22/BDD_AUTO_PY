# 🚀 BDD Automation Framework | Python & Selenium

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge\&logo=python\&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge\&logo=Selenium\&logoColor=white)
![Behave](https://img.shields.io/badge/Behave-BDD-blue?style=for-the-badge)
![UI/UX](https://img.shields.io/badge/UI/UX-Designer-orange?style=for-the-badge\&logo=figma)

Acest proiect reprezintă un framework de testare automată profesional, construit pentru a demonstra bunele practici în **QA Automation**. Folosește metodologia **BDD (Behavior Driven Development)** pentru a asigura transparența testelor între echipa tehnică și stakeholderi.

---

## 🏗️ Arhitectură: Page Object Model (POM)

Framework-ul este structurat modular pentru a facilita mentenanța și scalabilitatea:

| Componentă   | Locație      | Descriere                                                              |
| :----------- | :----------- | :--------------------------------------------------------------------- |
| **Features** | `features/`  | Scenarii Gherkin pentru Login și Books Management.                     |
| **Pages**    | `pages/`     | Încapsularea selectorilor și a logicii paginilor (Login, Home, Books). |
| **Steps**    | `steps/`     | Maparea pașilor din feature files către funcții Python.                |
| **Browser**  | `browser.py` | Gestionarea instanței de Selenium WebDriver.                           |
| **Context**  | `context.py` | Obiectul global pentru partajarea datelor în timpul rulării.           |

---

## 🛠️ Tehnologii și Unelte

* **Limbaj:** Python 3.12
* **Framework BDD:** Behave
* **Automatizare:** Selenium WebDriver
* **Pattern:** Page Object Model (POM)
* **IDE:** PyCharm

---

## 🚀 Instalare și Rulare Rapidă

### 1. Clonarea proiectului

```bash
git clone https://github.com/SanduAndreea22/BDD_AUTO_PY.git
cd BDD_AUTO_PY
```

### 2. Instalarea dependențelor

```bash
pip install behave selenium
```

### 3. Executarea testelor

```bash
behave
```

---

## 📝 Scenarii de Testare Implementate

* **Autentificare:** Verificarea fluxului de login cu diverse seturi de date.
* **Catalog Produse:** Navigarea și validarea elementelor din secțiunea de cărți.
* **UI Checks:** Testarea elementelor de interfață (Sidebar, Header) pentru integritate.

---


⭐ *Dacă acest framework ți-a fost util, nu uita să îi dai un Star pe GitHub!*
