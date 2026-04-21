class Studente:
    """
    Classe per la gestione della carriera accademica.
    Migliorata secondo gli standard del corso DiSUS.
    """
    def __init__(self, nome, cognome, eta, matricola, voti=None):
        self.nome = nome.title() # .title() mette le maiuscole a ogni parola (es. Giovanni Pio)
        self.cognome = cognome.title()
        self.eta = eta
        self.matricola = matricola
        self.voti = voti if voti is not None else []

    def __str__(self):
        return f"Studente: {self.nome} {self.cognome} (Matr: {self.matricola})"

    def presentati(self):
        sep = "=" * 60
        print(f"\n{sep}")
        print(f"🎓 PROFILO STUDENTE: {self.nome.upper()} {self.cognome.upper()}")
        print(f"   Età: {self.eta} | Matricola: {self.matricola}")
        print(f"   Libretto: {self.voti if self.voti else 'Vuoto'}")
        print(f"{sep}")

    def aggiungi_voto(self, nuovo_voto):
        if 18 <= nuovo_voto <= 30:
            self.voti.append(nuovo_voto)
            print(f"✅ Voto {nuovo_voto} registrato.")
        else:
            print(f"❌ Errore: {nuovo_voto} non è un voto valido.")

    def calcola_media(self):
        if not self.voti:
            print("⚠️ Libretto vuoto.")
            return 0.0
        media = sum(self.voti) / len(self.voti)
        print(f"📊 Media attuale: {media:.2f}")
        return media

    def valutazione_studio(self, ore):
        print(f"📖 Analisi studio ({ore} ore effettuate):")
        if ore > 10:
            status = "🔥 Eccellente! Sei prontissimo."
        elif ore > 5:
            status = "🟡 Buono, ma continua così."
        else:
            status = "🔴 Attenzione: studio insufficiente."
        print(f"   Esito: {status}\n")

# --- TEST DEL CODICE (Corretto per il terminale) ---
if __name__ == "__main__":
    # Creazione delle istanze (Sistemate le virgolette e gli spazi)
    studente1 = Studente("giovanni pio", "lonoce", 23, 20109166, [30, 30, 30, 30, 30])
    studente2 = Studente("giorgio", "giorgione", 22, 20102929, [30, 29, 25, 27])

    # Ciclo di test
    for s in [studente1, studente2]:
        s.presentati()
        s.calcola_media()
        s.aggiungi_voto(26)
        # Se il nome è Giovanni Pio (formattato title), diamogli 12 ore
        ore_studio = 12 if "Giovanni" in s.nome else 4
        s.valutazione_studio(ore_studio)
