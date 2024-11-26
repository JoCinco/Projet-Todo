
class todo_list:
    #Nommage de la liste
    def __init__(self, title):
        self.task = []
        self.title = title
    #Ajout d'une tâche unique
    def add_task(self, task_name):
        for task in self.task:
            if task['name'] == task_name:
                print(f"La tâche '{task_name}' existe déjà dans cette liste.")
                return
        self.task.append({'name': task_name, 'status': 'À faire'})
        print(f"'{task_name}' a été ajoutée à la ToDo-list.")
    #Suppression d'une tâche
    def remove_task(self, task_name):
        for task in self.task:
            if task['name'] == task_name:
                self.task.remove(task)
                print("La tâche", task , "a été retirée avec succès !")
                return
        else:
            print("Aucune tâche trouvée !")
    #Affichage de la liste entière
    def open_list(self):
        if self.task:
            print("Titre :",self.title)
            print("Tâches :")
            for task in self.task :
                print(f"- {task['name']}/*-*\{task['status']}")
        else:
            print("Le liste est vide ou inexistante !")
            return
    #Ajout de la fonctionnalité "Status"
    def status_modifier(self, task_name):
        for task in self.task:
            if task['status'] == 'À faire' :
                task['status'] == 'Fait'
            elif task['status'] == 'Fait':
                task['status'] == 'À faire'


liste_de_taches = todo_list("Notes pour le goûter")
liste_de_taches.open_list()
liste_de_taches.add_task("Faire des crêpes")
liste_de_taches.open_list()
liste_de_taches.remove_task("Faire des crêpes")
liste_de_taches.open_list()
liste_de_taches.add_task("Faire des cookies")
liste_de_taches.add_task("Faire des brownies")
liste_de_taches.open_list()
liste_de_taches.status_modifier("Faire des cookies")