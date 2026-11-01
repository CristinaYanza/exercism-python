"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    """Round all provided student scores."""
    resultados = []

    for nota in student_scores:
        resultados.append(round(nota))

    return resultados

def count_failed_students(student_scores):
    """Count the number of students who failed."""
    contador = 0

    for nota in student_scores:
        if nota <= 40:
            contador += 1

    return contador

def above_threshold(student_scores, threshold):
    """Return scores that are at or above the threshold."""
    mejores_notas = []

    for nota in student_scores:
        if nota >= threshold:
            mejores_notas.append(nota)

    return mejores_notas

def letter_grades(highest):
    """Create the lower thresholds for letter grades."""
    intervalo = (highest - 40) // 4

    return [
        41,
        41 + intervalo,
        41 + intervalo * 2,
        41 + intervalo * 3
    ]

def student_ranking(student_scores, student_names):
    """Organize students by rank, name, and score."""
    clasificacion = []

    for indice, nombre in enumerate(student_names):
        posicion = indice + 1
        nota = student_scores[indice]

        clasificacion.append(
            f"{posicion}. {nombre}: {nota}"
        )

    return clasificacion

def perfect_score(student_info):
    """Return the first student with a perfect score."""
    for estudiante in student_info:
        if estudiante[1] == 100:
            return estudiante

    return []