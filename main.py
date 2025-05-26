from input_handler import InputHandler
from output_handler import OutputHandler
from response_generator import ResponseGenerator

def main(
    input_handler=None,
    output_handler=None,
    response_generator=None
):
    """Función principal del chatbot, permite inyección de dependencias."""
    input_handler = input_handler or InputHandler()
    output_handler = output_handler or OutputHandler()
    response_generator = response_generator or ResponseGenerator()

    output_handler.send_output("¡Hola! Soy tu chatbot. Escribe 'salir' para terminar.")
    
    while True:
        user_input = input_handler.get_input()

        if user_input.lower() in ["salir", "adiós", "bye", "quit", "exit"]:
            output_handler.send_output("¡Hasta luego!")
            break

        response = response_generator.get_response(user_input)
        output_handler.send_output(response)

if __name__ == "__main__":
    main()

