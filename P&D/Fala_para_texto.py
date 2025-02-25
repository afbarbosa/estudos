import speech_recognition as sr
import time

def record_voice():
    mic = sr.Recognizer()
    phrase = ""  
    last_speech_time = time.time()  

    with sr.Microphone() as live_phone:
        mic.adjust_for_ambient_noise(live_phone)
        print("Estou ouvindo... Fale algo.")

        while True:
            try:
                audio = mic.listen(live_phone, phrase_time_limit=30)  
                text = mic.recognize_google(audio, language="pt-BR")

                if text:
                    phrase += text + " "  
                    last_speech_time = time.time()  
                    print("Você disse:", text)

            except sr.UnknownValueError:
                print("Não entendi, tente novamente.")
            
            except sr.RequestError:
                print("Erro ao acessar o serviço de reconhecimento de voz.")
                break  
            

            if time.time() - last_speech_time > 5:
                print("Pausa longa detectada. Finalizando...")
                break

    return phrase.strip() 

if __name__ == '__main__':
    phrase = record_voice()
    with open('texto.txt', 'w', encoding='utf-8') as file:
        file.write(phrase)
    print("Texto salvo em texto.txt:", phrase)
