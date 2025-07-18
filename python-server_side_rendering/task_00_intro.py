#!/usr/bin/python3

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Erreur : Le template doit être une chaîne de caractères.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Erreur : La liste des invités doit être une liste de dictionnaires.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):

        invitation = template
        champs = ["name", "event_title", "event_date", "event_location"]

        for champ in champs:
            valeur = attendee.get(champ)
            if not valeur:
                valeur = "N/A"
            invitation = invitation.replace("{" + champ + "}", str(valeur))

        nom_fichier = f"output_{index}.txt"
        try:
            with open(nom_fichier, 'w', encoding='utf-8') as fichier:
                fichier.write(invitation)
        except Exception as e:
            print(f"Erreur lors de l’écriture du fichier {nom_fichier} : {e}")
