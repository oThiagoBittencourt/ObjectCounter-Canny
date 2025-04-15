import cv2

def contar_objetos(imagem):
    """Tratamentos da Imagem"""
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    bordas = cv2.Canny(cinza, 50, 150)
    contornos, _ = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    """Resultados"""
    numero_objetos = len(contornos)

    imagem_contornos = imagem.copy()
    cv2.drawContours(imagem_contornos, contornos, -1, (0, 255, 0), 2)

    return numero_objetos, imagem_contornos

imagem = cv2.imread("Foto3.jpg")

if imagem is None:
    exit()

numero_objetos, imagem_contornos = contar_objetos(imagem)

cv2.imshow("Contornos", imagem_contornos)
print(f"Número de objetos detectados: {numero_objetos}")

cv2.waitKey(0)
cv2.destroyAllWindows()