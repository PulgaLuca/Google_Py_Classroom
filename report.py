from openpyxl import Workbook

class Report:
    @staticmethod
    def create_submission_report(students, submissions, output_excel):
        submission_status = {user_id: "YES" for user_id, _ in submissions}

        # Prepara i dati degli studenti
        student_data = []
        for user_id, full_name in students.items():
            nome, cognome = full_name.split(" ", 1) if " " in full_name else (full_name, "")
            submission = submission_status.get(user_id, "NO")
            grade = "-"
            student_data.append((nome, cognome, submission, grade))
        
        # Ordina i dati per cognome e poi per nome
        student_data.sort(key=lambda x: (x[1], x[0]))

        # Crea un nuovo workbook
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Submission Report"

        # Aggiungi l'intestazione
        sheet.append(["Nome", "Cognome", "Submission", "Grade"])

        # Popola i dati ordinati nel foglio
        for nome, cognome, submission, grade in student_data:
            sheet.append([nome, cognome, submission, grade])

        # Salva il file Excel
        workbook.save(output_excel)
        print(f"Report delle consegne creato: {output_excel}")
