# Clase base Persona que representa a una persona genérica en el sistema hospitalario
# Aplica el principio de responsabilidad única (SRP) al manejar solo atributos personales
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    # Método para mostrar la información personal
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}")

# Clase Paciente que hereda de Persona y agrega atributos específicos de un paciente
# Aplica el principio de herencia para extender funcionalidades sin modificar la clase base
class Paciente(Persona):
    def __init__(self, nombre, edad, genero, id_paciente, diagnostico):
        super().__init__(nombre, edad, genero)
        self.id_paciente = id_paciente
        self.diagnostico = diagnostico

    # Sobrescribe el método mostrar_info para incluir datos específicos del paciente
    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID Paciente: {self.id_paciente}, Diagnóstico: {self.diagnostico}")

# Clase Medico que hereda de Persona y añade atributos y métodos relacionados con su rol
# Aplica el principio de herencia y mantiene una única responsabilidad
class Medico(Persona):
    

    # Sobrescribe el método mostrar_info para incluir la especialidad del médico
    def mostrar_info(self):
        print(f'Médico: {self.nombre}, Especialidad: {self.especialidad}')
       

    # Método para atender a un paciente, demostrando interacción entre clases
    def atender_paciente(self, paciente):
        print(f'Atendiendo al paciente {paciente}')
       

# Clase principal que orquesta la interacción entre pacientes y médicos
# Aplica el principio de inversión de dependencias al instanciar las clases específicas
class SistemaHospital:
    def __init__(self):
        self.medicos = []

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def ejecutar(self):
        # Mostrar información del médico
        for medico in self.medicos:
            medico.mostrar_informacion()

        # Simular la atención médica
        for medico in self.medicos:
            medico.atender_paciente('Paciente Ejemplo')

# Punto de entrada principal del programa
# Garantiza que el código solo se ejecuta cuando el script es ejecutado directamente
if __name__ == "__main__":
    sistema = SistemaHospital()
    sistema.agregar_medico(Medico('Dr. Smith', 'Cardiología'))
    sistema.agregar_medico(Medico('Dr. Johnson', 'Neurología'))
    sistema.ejecutar()
