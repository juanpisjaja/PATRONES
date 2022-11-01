# PYTHON SINGLETON

## ***Que es?***
> **Singleton se le denomina a un patron de diseño que le permite crear un sola instancia de una clase. Aparte de esto tiene muchos beneficios, algunos de ellos son:** 

![Image text](https://refactoring.guru/images/patterns/content/singleton/singleton-comic-1-es.png?id=cc859f28938dcdbd30d5149a9d916060)

1. Para limitar el acceso simultáneo a un recurso compartido.
2. Para crear un punto de acceso global para un recurso.
3. Para crear solo una instancia de una clase, a lo largo de la vida útil de un programa.

> Todas las implementaciones del patrón Singleton tienen estos dos pasos en común:

1. Hacer privado el constructor por defecto para evitar que otros objetos utilicen el operador new con la clase Singleton.
2. Crear un método de creación estático que actúe como constructor. Tras bambalinas, este método invoca al constructor privado para crear un objeto y lo guarda en un campo estático. Las siguientes llamadas a este método devuelven el objeto almacenado en caché.

# Ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/singleton.png)
***

# PYTHON PROXY

## ***Que es?***
> **Proxy es un patrón de diseño estructural que proporciona un objeto que actúa como sustituto de un objeto de servicio real utilizado por un cliente. Un proxy recibe solicitudes del cliente, realiza parte del trabajo (control de acceso, almacenamiento en caché, etc.)**

![Image text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_rXiavL7z9jP_5QEcExG4kBSfWMhxxvGfxt3Az3jgxehSIpvt3NHSaqFTt6j_3HaIhMc&usqp=CAU)

>Aunque el patrón Proxy no es un invitado habitual en la mayoría de aplicaciones Python, resulta de mucha utilidad en algunos casos especiales. Es insustituible cuando queremos añadir algunos comportamientos adicionales a un objeto de una clase existente sin cambiar el código cliente.

# Ejemplo funcional
![ejemplo funcional]([https://github.com/juanpisjaja/PATRONES/blob/main/img/singleton.png](https://github.com/juanpisjaja/PATRONES/blob/main/img/proxy.png)
***

# PYTHON PROTOTIPO

## ***Que es?***
>**El método de prototipo es un patrón de diseño de creación que tiene como objetivo reducir el número de clases utilizadas para una aplicación. Le permite copiar objetos existentes independientemente de la implementación concreta de sus clases. Generalmente, aquí el objeto se crea copiando una instancia prototípica durante el tiempo de ejecución.**

* Se recomienda encarecidamente utilizar el método Prototype cuando la creación del objeto es una tarea costosa en términos de tiempo y uso de recursos y ya existe un objeto similar.

![Image text](https://python2017.files.wordpress.com/2017/08/problema.png)

### Ventajas 
1. Menor número de subclases.
2. Proporciona valores variables a nuevos objetos.
3. Proporciona una estructura variable a nuevos objetos.

# Ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/prototipo.png)
***

# PYTHON OBSERVADOR

## ***Que es?***
>**El método del observador es un patrón de diseño de comportamiento que le permite definir o crear un mecanismo de suscripción para enviar la notificación a los múltiples objetos sobre cualquier evento nuevo que le suceda al objeto que están observando.**

* El patrón Observer permite que el objeto editor de texto notifique a otros objetos de servicio sobre los cambios en su estado.

![Image text](https://stackabuse.s3.amazonaws.com/media/observer-design-pattern-in-python-01.jpg)

### Pros y Contras 
1. Principio abierto/cerrado . Puede introducir nuevas clases de suscriptores sin tener que cambiar el código del editor (y viceversa si hay una interfaz de editor).
2. Puede establecer relaciones entre objetos en tiempo de ejecución.

# ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/observador.png)
***

# PYTHON MVC

## ***Que es?***
> **La arquitectura MVC como podemos encontrar en cualquier sitio web referente al diseño de software es un patrón arquitectural es decir que nos dicta una arquitectura como modelo o guía para el desarrollo de aplicaciones.**

> Esta arquitectura nos dicta como se estructura cada uno de los componentes de nuestro software, las responsabilidades de cada uno y las relaciones entre ellos.

![Image text](https://i.stack.imgur.com/JFN82.png)

* Funcional porque cada bloque de código se ubicará dentro del componente según su función o rol. Es decir, mas claramente no podrás mezclar el código de la parte visual (estilos, colores, fuentes, imágenes) con la parte de los datos (código de lenguaje SQL) ni con la parte lógica que controla la interacción entre estos otros dos componentes (Por ejemplo la función que muestra un archivo según se visite una url). 

# Ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/mvc.png)
***

# PYTHON MEMENTO

## ***Que es?***
>**Memento es un patrón de diseño de comportamiento que permite tomar instantáneas del estado de un objeto y restaurarlo en el futuro.**

### Aplicabilidad 
* Utiliza el patrón Memento cuando quieras producir instantáneas del estado del objeto para poder restaurar un estado previo del objeto.

* El patrón Memento te permite realizar copias completas del estado de un objeto, incluyendo campos privados, y almacenarlos independientemente del objeto. Aunque la mayoría de la gente recuerda este patrón gracias al caso de la función Deshacer, también es indispensable a la hora de tratar con transacciones (por ejemplo, si debes volver atrás sobre un error en una operación).

* Utiliza el patrón cuando el acceso directo a los campos, consultores o modificadores del objeto viole su encapsulación.

![Image text](https://refactoring.guru/images/patterns/cards/memento-mini-3x.png)

### Pros y Contras 
1. +Puedes producir instantáneas del estado del objeto sin violar su encapsulación.
2. -La aplicación puede consumir mucha memoria RAM si los clientes crean mementos muy a menudo.
3. +Puedes simplificar el código de la originadora permitiendo que la cuidadora mantenga el historial del estado de la originadora.
4. -Las cuidadoras deben rastrear el ciclo de vida de la originadora para poder destruir mementos obsoletos.

# Ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/memento.png)
***

# PYTHON INYECCION DE DEPENDENCIAS 

## ***Que es?***
>**La inyección de dependencia es un técnica de desarrollo que nos permite escribir código con un alto nivel de cohesión y un bajo nivel de dependencia.**

* Para comprender el tema de inyección de dependencias es ver a las dependencias cómo si de piezas de lego se tratasen. Pudiendo reemplazarla unas por otras dependiendo de nuestras necesidades.

1. Veamos un ejemplo.

class Monitor:
    pass

class Computadora:
    def __init__(self):
       self.monitor= Monitor() # <-- dependency

![Image text](https://desarrolloweb.com/articulos/images/poo/figura2-id.jpg)

# Ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/inyeccion%20de%20dependencia%20.png)
***

# PYTHON FACHADA 

## ***Que es?***
>**El método de fachada es un patrón de diseño estructural que proporciona una interfaz unificada más simple a un sistema más complejo. La palabra Fachada significa la cara de un edificio o, en particular, una interfaz exterior de un sistema complejo, que consta de varios subsistemas.**

### Ventajas 
1. Aislamiento: podemos aislar fácilmente nuestro código de la complejidad de un subsistema.
2. Proceso de prueba: el uso del método de fachada hace que el proceso de prueba sea comparativamente fácil, ya que tiene métodos convenientes para las tareas de prueba comunes.
3. Acoplamiento suelto: disponibilidad de acoplamiento suelto entre los clientes y los subsistemas.

### Desventajas 
1. Cambios en los métodos: como sabemos que en el método Facade , los métodos posteriores se adjuntan a la capa de Fachada y cualquier cambio en el método posterior puede traer cambios en la capa de Fachada que no es favorable.
2. Proceso costoso: no es barato establecer el método Facade en nuestra aplicación para la confiabilidad del sistema.
3. Violación de las reglas: siempre existe el temor de violar la construcción de la capa de fachada.

![Image text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsiRVaUTddiFGGx2MJ0KvmONTszr5vqzdo9Q&usqp=CAU)

# Ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/fachada.png)
***

# PYTHON FABRICA ABSTRACTA 

## ***Que es?***
>**Abstract Factory es un patrón de diseño creacional que resuelve el problema de crear familias completas de productos sin especificar sus clases concretas.**

![Image text](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-es.png?id=0378c9faca39afa20e41a4d37e7e3828)

### Inplementacion
1. Trace una matriz de distintos tipos de productos frente a las variantes de estos productos.
2. Declare interfaces de productos abstractos para todos los tipos de productos. Luego haga que todas las clases de productos concretos implementen estas interfaces.
3. Declare la interfaz de fábrica abstracta con un conjunto de métodos de creación para todos los productos abstractos.
4. Implemente un conjunto de clases de fábrica concretas, una para cada variante de producto

# Ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/fabracia%20abstracta.png)
***

# PYTHON FABRICA 

## ***Que es?***
>**Factory Method es un patrón de diseño creacional que proporciona una interfaz para crear objetos en una superclase, mientras permite a las subclases alterar el tipo de objetos que se crearán.**

### Aplicabilidad
1. Utiliza el Método Fábrica cuando no conozcas de antemano las dependencias y los tipos exactos de los objetos con los que deba funcionar tu código.
2. El patrón Factory Method separa el código de construcción de producto del código que hace uso del producto. Por ello, es más fácil extender el código de construcción de producto de forma independiente al resto del código.
3. Por ejemplo, para añadir un nuevo tipo de producto a la aplicación, sólo tendrás que crear una nueva subclase creadora y sobrescribir el Factory Method que contiene.

![Image text](https://media.geeksforgeeks.org/wp-content/uploads/20200116152733/solution_factory-_diagram.png)

### Pros  y Contras 
1. +Evitas un acoplamiento fuerte entre el creador y los productos concretos.
2. +Principio de responsabilidad única. Puedes mover el código de creación de producto a un lugar del programa, haciendo que el código sea más fácil de mantener.
3. -Puede ser que el código se complique, ya que debes incorporar una multitud de nuevas subclases para implementar el patrón. La situación ideal sería introducir el patrón en una jerarquía existente de clases creadoras.

# Ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/fabrica.png)
***

# PYTHON ESTRATEGIA 

## ***Que es?***
>**El método de estrategia es el patrón de Behavioural Design que permite definir la familia completa de algoritmos, encapsula cada uno y coloca cada uno de ellos en clases separadas y también permite intercambiar sus objetos.**

### Ventajas
* Principio abierto / cerrado.
* Encapsulación.
### Desventajas 
* Creación de objetos adicionales.
* Conciencia entre los clientes.
* Aumenta la complejidad.

![Image text](https://empresas.blogthinkbig.com/wp-content/uploads/2020/04/image-8.png?resize=552%2C260)

### Aplicabilidad
1. Muchas clases similares: este método es muy preferido cuando tenemos muchas clases similares que difieren en la forma en que se ejecutan.
2. Conquistar el aislamiento: generalmente se usa para aislar la lógica de negocios de la clase de la implementación algorítmica.

# Ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/estrategia.png)
***

# PYTHON DECORADOR 

## ***Que es?***
>**Los decoradores forman parte de Python desde la versión 2.4 y cómo dice Michele Simionato nos aportan lo siguiente: Reducen el código común y repetitivo (el llamado código boilerplate). Favorecen la separación de responsabilidades del código. Aumentan la legibilidad y la mantenibilidad**

### Podemos dividir los decoradores en grupos 

1. Según los parámetros que admiten:
    * No admiten parámetros
    * Sí admiten parámetros
2. Según si preservan la firma o signatura del método al que decoran:
    * Decoradores no que preservan la firma
    * Decoradores que sí la preservan

![Image text](https://recursospython.com/wp-content/uploads/2018/06/decoradores-python.png)

* _Ejemplo de manera larga_ 
def forat_negre(f):
    def none(*args, **kw_args):
        pass
    none.__doc__= f.__doc__
    none.__dict__= f.__dict__
    none.__name__= f.__name__
    return none

# Ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/decorador.png)
***

# PYTHON DAO

## ***Que es?***
>**El patrón Arquitectónico Data Access Object (DAO), el cual permite separar la lógica de acceso a datos de los Objetos de negocios (Bussines Objects), de tal forma que el DAO encapsula toda la lógica de acceso de datos al resto de la aplicación.**

### Problemática
>Una de las grandes problemáticas al momento de acceder a los datos, es que la implementación y formato de la información puede variar según la fuente de los datos. 

### Solución
>Dado lo anterior, el patrón DAO propone separar por completo la lógica de negocio de la lógica para acceder a los datos, de esta forma, el DAO proporcionará los métodos necesarios para insertar, actualizar, borrar y consultar la información.

![Image text](https://i.ytimg.com/vi/VVbTSkzhtA8/maxresdefault.jpg)

# Ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/DAO.png)
***

# PYTHON COMMAND

## ***Que es?***
>**Command es un patrón de diseño de comportamiento que convierte una solicitud en un objeto independiente que contiene toda la información sobre la solicitud. Esta transformación te permite parametrizar los métodos con diferentes solicitudes, retrasar o poner en cola la ejecución de una solicitud y soportar operaciones que no se pueden realizar.**

### Pseudocodigo
>En este ejemplo, el patrón Command ayuda a rastrear el historial de operaciones ejecutadas y hace posible revertir una operación si es necesario.

### Pros y Contras
1. Principio de responsabilidad única. Puedes desacoplar las clases que invocan operaciones de las que realizan esas operaciones.
2. Principio de abierto/cerrado. Puedes introducir nuevos comandos en la aplicación sin descomponer el código cliente existente.
3. El código puede complicarse, ya que estás introduciendo una nueva capa entre emisores y receptores.

![Image text](https://www.wikihow.com/images_en/thumb/8/80/Use-Windows-Command-Prompt-to-Run-a-Python-File-Step-10.jpg/v4-460px-Use-Windows-Command-Prompt-to-Run-a-Python-File-Step-10.jpg.webp)

# ejemplo funcional
![ejemplo funcional](https://github.com/juanpisjaja/PATRONES/blob/main/img/command.png)
***
























