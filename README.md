# SoftwareEng2021

Skriv en kort forklaring på hva du gjorde
---
* Jeg lagde et nytt repository i Github
* I det nye repositoriet så åpnet jeg en ferdiglaget workflow som var tilgjengelig under Actions
* Deretter la jeg til Oblig 2 som innholdt boolIsLeapYear og tester for den, inn i samme repository
* Jeg gjorde commits både for å sjekke om det funket eller ikke (når testene var feil), og at testene ble kjørt dersom man commitet/pushet noe til Github

---

## Repository - Innhold

```bash
├── github
│   └── workflows
│       └── python-app.yml
├── Oblig2
│   └── test
│       ├── __pycache__
|       |      └── ...
│       ├── boolisLeapYear.py
|       └── test_boolisLeapYear.py
│   ├── main.py
│   └── requirements.txt
├── README.md
└── .gitignore
```

---
### Gå til Github -> Actions for å se kjøring av tester og at de passerer (eller ikke)
