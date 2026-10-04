"""Modulos 07 a 10 del curso.

Tercer bloque de contenido; ver _curso_datos.py y _curso_datos_b.py.
"""

MODULOS_C = [
    # ------------------------------------------------------------------ 07
    {
        "num": "07",
        "titulo": "Robot para mantenimiento",
        "lead": (
            "El salto de la inspección pasiva a la intervención física: qué "
            "significa que un robot toque un activo, y qué hay que tener resuelto "
            "antes de intentarlo."
        ),
        "resumen": "De la inspección pasiva a la intervención física sobre la red.",
        "icono": "wrench",
        "meta": [
            ("clock", "90 min de lectura"),
            ("doc", "Módulo 7 de 10"),
            ("wrench", "Intervención sobre el activo"),
        ],
        "objetivos": [
            "Definir qué significa que un robot intervenga sobre una red, y por qué es un cambio de categoría de riesgo.",
            "Distinguir los tres niveles de intervención sobre una línea, del más simple al más complejo.",
            "Identificar las condiciones que deben cumplirse para que una intervención sea aceptable.",
            "Construir el procedimiento y la trazabilidad que exige una intervención de robot.",
        ],
        "secciones": [
            {
                "h2": "Por qué intervenir es otra categoría",
                "html": """
            <p>Un robot que <em>mira</em> un activo no puede dañarlo más allá de lo que lo dañaría tocarlo. Un robot que <em>actúa</em> sobre el activo puede dejarlo fuera de servicio, puede dejar un aflojamiento que provoque una falla semanas después, o puede aplicar el par incorrecto a un componente que no lo tolera.</p>
            <p>Esa es la razón por la que la intervención robotizada no es "el siguiente paso natural" después de la inspección, aunque comercialmente se presente así. Es un proyecto nuevo, con su propio análisis de riesgo, su propio procedimiento y su propia evidencia.</p>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-shield"/></svg>El principio que no se negocia</p>
              <p>Todo lo que el módulo 8 y los procedimientos de la empresa digan sobre seguridad eléctrica se aplican <em>igual</em> cuando quien ejecuta es un robot. La autonomía cambia quién hace la tarea y cómo se registra, nunca bajo qué reglas se hace.</p>
            </div>
                """,
            },
            {
                "h2": "Los tres niveles de intervención",
                "html": """
            <p>No todas las intervenciones tienen la misma dificultad. Ordenarlas es la mejor forma de decidir por dónde empezar.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Nivel</th><th>Qué hace</th><th>Riesgo para el activo</th><th>Requisito previo</th></tr>
                </thead>
                <tbody>
                  <tr><td>Nivel 1 — Contacto no invasivo</td><td>Limpieza del aislador, retiro de contaminación, aplicación de producto.</td><td>Mínimo: no cambia la función del componente.</td><td>Inspección previa que confirme que el componente está sano.</td></tr>
                  <tr><td>Nivel 2 —Ajuste mecánico</td><td>Apriete de pernos a par especificado, alineación de un herraje.</td><td>Medio: un par incorrecto deja un aflojamiento futuro.</td><td>Par de apriete documentado y sensor de torque con registro.</td></tr>
                  <tr><td>Nivel 3 — Sustitución</td><td>Cambio de aislador, conector o grapa.</td><td>Alto: una sustitución mal hecha es una falla diferida.</td><td>Componente de reemplazo, procedimiento probado y validación previa.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>Recomendación de entrada</p>
              <p>Empiece por el <strong>nivel 1</strong>. La limpieza de aisladores es la intervención con el mejor balance del catálogo: valor real para el activo, riesgo bajo, y es además la que más información devuelve, porque revela defectos que estaban ocultos bajo la contaminación.</p>
            </div>
                """,
            },
            {
                "h2": "Intervención en línea energizada y desenergizada",
                "html": """
            <p>La distinción no es técnica, es de procedimiento, y es donde la mayoría de los proyectos se complica.</p>
            <ul class="bullets">
              <li><strong>Línea desenergizada:</strong> el.robot puede acercarse más, el riesgo de arco eléctrico baja y el procedimiento es el de un trabajo en caliente común. Es el escenario de entrada razonable para las primeras intervenciones.</li>
              <li><strong>Línea energizada:</strong> cualquier intervención exige distances de seguridad, control de la zona de trabajo y un procedimiento specifico aprobado. No es un problema de obstáculo técnico: es un problema de autorización.</li>
            </ul>

            <div class="callout callout-warn">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-shield"/></svg>Advertencia</p>
              <p>Cualquier proyecto que proponga intervención sobre línea energizada antes de haber acumulado historial de intervención sobre línea desenergizada está saltándose la etapa de aprendizaje. La secuencia natural es: inspeccionar, luego Cleaning en desenergizado, luego ajuste, y solo después considerar la energizada.</p>
            </div>
                """,
            },
            {
                "h2": "Herramientas y control de par",
                "html": """
            <p>En el nivel 2, la diferencia entre una intervención correcta y una falla diferida es el par aplicado. Y el par aplicado por un brazo robótico con retroalimentación de posición no es el mismo que aplica una llave dinamométrica.</p>

            <dl class="glossary">
              <div><dt>Torque de apriete</dt><dd>El momento de fuerza que se aplica al perno. Depende del diámetro del perno y de la clase de acero. Un valor incorrecto, por alto, termina rompiendo el hilo; por bajo, deja el aflojamiento que el calor va a terminar desarrollando.</dd></div>
              <div><dt>Sensor de torque</dt><dd>El instrumento que mide el par realmente aplicado y lo registra. Sin sensor de torque, no hay evidencia de que el apriete ocurrió, solo de que el robot movió la herramienta.</dd></div>
              <div><dt>Curva de apriete</dt><dd>El perfil de par a lo largo del tiempo. En un perno nuevo, el par crece linealmente; en uno que ya fue apretado, cae. El robot puede diferenciar ambos casos, y esa es información valiosa.</dd></div>
            </dl>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>El argumento de trazabilidad</p>
              <p>El valor real del apriete robotizado no es que apriete: es que <strong>registra el par de cada perno</strong>, con sello de tiempo y posición, y lo deja en un expediente. Una cuadrilla que aprieta deja una nota; un robot deja evidencia auditable. Eso es lo que un auditor de calidad reconoce y lo que justify el costo del sistema.</p>
            </div>
                """,
            },
            {
                "h2": "Trazabilidad de la intervención",
                "html": """
            <p>Intervenir sin registro es peor que no intervenir, porque genera la impresión de que el trabajo se hizo. La trazabilidad mínima de una intervención robotizada incluye:</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Registro</th><th>Qué contiene</th><th>Por qué lo exige la calidad</th></tr>
                </thead>
                <tbody>
                  <tr><td>Identificación</td><td>Torre, componente, posición, orientación.</td><td>Para que el hallazgo sea localizable en el futuro.</td></tr>
                  <tr><td>Parámetro de proceso</td><td>Torque aplicado, ángulo final, número de vueltas.</td><td>Para verificar que se cumplió la especificación.</td></tr>
                  <tr><td>Evidencia visual</td><td>Foto antes, foto después, del componente intervenido.</td><td>Para el expediente técnico y para auditorías.</td></tr>
                  <tr><td>Resultado del control</td><td>Verificación posterior: tensión de línea, termografía, etc.</td><td>Para confirmar que la intervención resolvió el problema.</td></tr>
                  <tr><td>Sello de tiempo y operador</td><td>Cuándo y quién autorizó la intervención.</td><td>Para la cadena de responsabilidad.</td></tr>
                </tbody>
              </table>
            </div>
                """,
            },
        ],
        "taller": {
            "titulo": "Taller: procedimiento de cambio de componente",
            "html": """
            <p>Se redacta, en detalle, el procedimiento de una intervención de nivel 3 —un cambio de aislador en línea desenergizada— siguiendo la estructura de un procedimiento real de mantenimiento. El objetivo es entender cuánto procedimiento hay detrás de lo que parece una tarea simple.</p>
            <ol class="steps">
              <li><strong>Precondiciones.</strong> Línea desenergizada, bloqueada, verificada; permiso de trabajo emitido; acceso a la base asegurado.</li>
              <li><strong>Inspección previa.</strong> Confirmar que el componente a cambiar está efectivamente en falla, con evidencia registrada.</li>
              <li><strong>Verificación de repuesto.</strong> El componente de reemplazo existe, es compatible y está en el sitio antes de subir el robot.</li>
              <li><strong>Secuencia de desmontaje.</strong> El orden de afloje, con el torque de cada perno y el registro de cada uno.</li>
              <li><strong>Secuencia de montaje.</strong> El orden inverso, con verificación de torque y, si aplica, control de par por método angular.</li>
              <li><strong>Verificación posterior.</strong> Termografía del punto intervenido y comprobación de que la estructura quedó en su posición.</li>
              <li><strong>Cierre y expediente.</strong> Registro consolidado y actualización del historial del componente.</li>
            </ol>
            <p>Si el procedimiento completo no cabe en dos páginas, probablemente el alcance de la intervención es demasiado amplio para el nivel de madurez del equipo.</p>
            """,
            "entrega": (
                "Procedimiento de cambio de componente de dos páginas, con precondiciones, secuencia, torques, "
                "puntos de verificación y requisitos de registro."
            ),
        },
        "resumen_html": """
            <p>Para la gerencia, el mensaje de este módulo es que <strong>la intervención robotizada no es un producto que se compra, es una capacidad que se construye</strong>. No hay un robot en el mercado que pueda cambiar un aislador en una torre sin un procedimiento detrás, y ese procedimiento es el trabajo de verdad.</p>
            <p>LaBuena noticia es que la secuencia es segura: se empieza inspeccionando, se sigue con tareas de contacto no invasivo, luego con ajuste mecánico, y solo al final se considera la sustitución. Cada nivel da información del anterior. Un programa que respeta esa secuencia acumula evidencia y no acumula accidentes.</p>
        """,
    },

    # ------------------------------------------------------------------ 08
    {
        "num": "08",
        "titulo": "Seguridad eléctrica",
        "lead": (
            "Distancia de seguridad, compatibilidad electromagnética y las "
            "condiciones de campo que un robot de red tiene que demostrar antes de "
            "operar cerca de un conductor."
        ),
        "resumen": "Distancia de seguridad, compatibilidad electromagnética y recuperación en campo.",
        "icono": "shield",
        "meta": [
            ("clock", "90 min de lectura"),
            ("doc", "Módulo 8 de 10"),
            ("shield", "Seguridad y conformidad"),
        ],
        "objetivos": [
            "Enumerar las cinco capas de seguridad que debe tener un robot de red, de la más externa a la más interna.",
            "Explicar por qué la compatibilidad electromagnética no es un trámite, sino una condición de existencia del producto.",
            "Describir el comportamiento seguro esperado ante pérdida de comunicación, de energía y de posicionamiento.",
            "Construir la_argumentación de seguridad de un piloto ante un comité que va a preguntar qué pasa si falla.",
        ],
        "secciones": [
            {
                "h2": "Las cinco capas de seguridad",
                "html": """
            <p>Un robot de red no se protege con un solo mecanismo. La seguridad es el conjunto de capas, y cada una cubre un fallo que las otras no cubren.</p>

            <ol class="steps">
              <li><strong>Diseño y certificación.</strong> El equipo cumple los requisitos de la norma aplicable y los de seguridad eléctrica del país donde opera. Es la capa que se demuestra con documentos.</li>
              <li><strong>Restricción del entorno.</strong> El robot no se despliega en cualquier sitio: hay condiciones de viento, de temperatura, de superficie y de proximity al conductor que se verifican antes de salir.</li>
              <li><strong>Detectores a bordo.</strong> Sensores que miden en todo momento la distancia al conductor y a la estructura, con umbrales que disparan la parada.</li>
              <li><strong>Parada segura.</strong> Cuando algo se dispara, el robot no se apaga: se detiene de forma controlada, con la carga en posición segura, y queda en un estado definido.</li>
              <li><strong>Recuperación.</strong> Un procedimiento documentado para devolver el sistema a operación, y para el caso en que no se pueda, que es el más frecuente.</li>
            </ol>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>La pregunta que siempre llega</p>
              <p>"¿Qué pasa si el robot se cae?" No es la pregunta más difícil. La más difícil es <strong>"¿qué pasa si el robot se queda sin comunicación?"</strong>, porque la respuesta honesta es que el robot debe saber qué hacer sin nadie que le diga, y eso hay que demostrarlo en pruebas, no en el diseño.</p>
            </div>
                """,
            },
            {
                "h2": "Distancia y zona de trabajo",
                "html": """
            <p>La distancia mínima entre un conductor y cualquier objeto lo fija la tensión de la línea, y no es negociable. Lo que el robot tiene que Respect es ese número, automáticamente, en todo momento.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Concepto</th><th>Qué significa</th><th>Cómo lo controla el robot</th></tr>
                </thead>
                <tbody>
                  <tr><td>Distancia mínima de trabajo</td><td>La separación mínima entre el conductor energizado y cualquier parte del equipo o persona.</td><td>Sensor de distancia con alarma y parada.</td></tr>
                  <tr><td>Distancia de seguridad</td><td>Una separación mayor, de margen, paraXu-PR accommodate errores de medición y movimiento.</td><td>Distancia interna del sistema, menor que la mínima teórica.</td></tr>
                  <tr><td>Límite de aproximación</td><td>El valor que el software impide rebasar.</td><td>Restricción de software no modificable por el operador.</td></tr>
                  <tr><td>Zona de trabajo</td><td>El área definida alrededor de la línea dentro de la cual se requieren permisos y controles.</td><td>Delimitación geográfica y señalización en campo.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout callout-warn">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-shield"/></svg>Los valores dependen de la norma local</p>
              <p>Este módulo no publica distancias numéricas porque <strong>cada país tiene sus propias reglas</strong> y además difieren por tensión y por condición de línea. Lo que debe hacer cualquier proyecto es tomar el valor del reglamento que le aplica, documentarlo como requisito de diseño y verificarlo en campo con el instrumento que la propia empresa usa para medirlo.</p>
            </div>
                """,
            },
            {
                "h2": "Compatibilidad electromagnética: la condición de existencia",
                "html": """
            <p>Un robot de red trabaja junto a fuentes de campo electromagnético notoriously hostiles: campos magnéticos intensos de corriente alterna, descargas atmosféricas, subestaciones, y radios de comunicaciones en la misma frecuencia que su enlace.</p>
            <p>De ahí vienen dos familias de problemas que no son opcionales:</p>
            <ul class="bullets">
              <li><strong>Inmunidad:</strong> el equipo debe seguir funcionando correctamente aunque el ambiente electromagnético loРУROLLIecte. La conformidad con las normas de inmunidad de uso industrial es el mínimo.</li>
              <li><strong>Emisiones:</strong> el equipo no debe emitir más de lo permitido, porque en un ambiente de subestación puede interferir con otros sistemas de proteccion o comunicaciones críticas.</li>
              <li><strong>Descarga electrostática:</strong> una pregunta de campo clásica enaltitude baja y sequedad.</li>
              <li><strong>Interferencia con otros sistemas:</strong> incluyendo el propio enlace de datos del robot y cualquier sistema de proteccion instalado en la subestación.</li>
            </ul>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>Por qué esto no es un trámite</p>
              <p>La conformidad en EMC no es un sello que se pega al producto. Es la evidencia de que el equipo <strong>funciona</strong> en el ambiente para el que fue diseñado. Un robot que funciona en taller y falla a 200 metros de una subestación no tiene un problema de certificación: tiene un problema de diseño que la certificación habría detectado.</p>
            </div>
                """,
            },
            {
                "h2": "Fallas en campo y comportamiento seguro",
                "html": """
            <p>La seguridad de un robot se juzga por su comportamiento en el peor caso, no en el mejor. Estos son los escenarios que deben tener respuesta documentada y probada.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Falla</th><th>Comportamiento seguro esperado</th><th>Qué hay que demostrar</th></tr>
                </thead>
                <tbody>
                  <tr><td>Pérdida de enlace de comunicaciones</td><td>Detección de ausencia de enlace y comportamiento definido: parar, seguir, o volver al punto de origen.</td><td>Que el tiempo de detección es menor que el tiempo que el robot está expuesto sin control.</td></tr>
                  <tr><td>Pérdida de posicionamiento</td><td>El robot no debe operar si no sabe dónde está. Detección y parada o retorno, no operación a ciegas.</td><td>Que no hay modo de fallo en el que el robot actué sin localization válida.</td></tr>
                  <tr><td>Falla de batería</td><td>Descenso controlado a la posición segura, no caída libre.</td><td>Que el robot llega a un estado seguro en el modo de falla más adverso.</td></tr>
                  <tr><td>Atasco mecánico</td><td>Detección de exceso de esfuerzo y retroceso controlado.</td><td>Que el límite de torque protege la estructura, no solo el robot.</td></tr>
                  <tr><td>Viento sobre el límite</td><td>El robot no debe operar con viento por encima de su umbral, y debe poder recuperarse si aparece.</td><td>Que el umbral es un bloqueo, no una recomendación.</td></tr>
                  <tr><td>Parada de emergencia</td><td>Corte inmediato de movimiento, con categoría de parada definida.</td><td>Que es accesible desde el campo y que el estado posterior es conocido.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-doc"/></svg>Práctica recomendada</p>
              <p>Ninguna de estas respuestas se acepta en un documento: se demuestran con pruebas, en el entorno real, y se registran. Un piloto de seguridad que no incluye pruebas de falla no es un piloto de seguridad, es una demostración.</p>
            </div>
                """,
            },
        ],
        "taller": {
            "titulo": "Taller: análisis de riesgo del piloto",
            "html": """
            <p>Se construye el análisis de riesgo del piloto de forma estructurada, como lo haría un comité antes de autorizar la salida del robot. El entregable es el documento que realmente decide si el proyecto arranca.</p>
            <ol class="steps">
              <li><strong>Describa el escenario:</strong> activo, tarea, condiciones del entorno, hora del día, personal en la zona.</li>
              <li><strong>Liste los peligros:</strong> eléctricos, mecánicos, de caída, de clima, de pérdida de comunicaciones, de operador.</li>
              <li><strong>Evalúe cada peligro:</strong> probabilidad y severidad, con la escala de la propia empresa.</li>
              <li><strong>Asigne una barrera por peligro:</strong> capa de prevención y capa de mitigación, según el módulo.</li>
              <li><strong>Identifique los riesgos residuales:</strong> los que quedan después de las barreras, y decida si se aceptan.</li>
              <li><strong>Defina las condiciones de parada del piloto:</strong> qué señal, de quién, obliga a detener la operación y revisar.</li>
            </ol>
            <p>El paso 5 es el que más revela sobre el estado real de la tecnología. Un riesgo residual alto y aceptado por necesidad operativa es una decisión legítima; un riesgo residual alto que nadie discutió es un defecto del proceso.</p>
            """,
            "entrega": (
                "Análisis de riesgo del piloto: peligros, evaluación, barreras por capa, riesgos residuales "
                "aceptados y condiciones de parada."
            ),
        },
        "resumen_html": """
            <p>Para la gerencia, el mensaje es que <strong>la seguridad no es un requisito del producto, es una condición de autorización</strong>. Ningún robot de red opera porque su fabricante lo certifique: opera porque la empresa analizó el riesgo, aceptó los riesgos residuales y definó las condiciones bajo las cuales se detiene.</p>
            <p>Ese documento, que es un trámite para mucha gente, es en realidad el que hace posible el proyecto. Y es también el que le va a permitir a la empresa decir, meses después, por qué autorizó lo que autorizó.</p>
        """,
    },

    # ------------------------------------------------------------------ 09
    {
        "num": "09",
        "titulo": "Diseño del primer prototipo",
        "lead": (
            "Componentes, controladores y telemetría para construir la primera "
            "versión, y las decisiones de ingeniería que más conviene acertar."
        ),
        "resumen": "Componentes, controladores y telemetría para construir la primera versión.",
        "icono": "cpu",
        "meta": [
            ("clock", "90 min de lectura"),
            ("doc", "Módulo 9 de 10"),
            ("cpu", "Arquitectura del sistema"),
        ],
        "objetivos": [
            "Describir la arquitectura completa de un robot de red, desde la mecánica hasta la nube.",
            "Elegir entre controlador de consumo, embebido y controlador industrial, con criterios claros.",
            "Dimensionar la telemetría según el volumen de datos y la cobertura del tramo.",
            "Identificar las tres decisiones de diseño que, una vez tomadas, son caras de revertir.",
        ],
        "secciones": [
            {
                "h2": "La arquitectura completa",
                "html": """
            <p>Un robot de red es un sistema de seis bloques. Lo que suele fallar en los prototipos no es ningún bloque aislado, sino las interfaces entre ellos.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Bloque</th><th>Responsabilidad</th><th>Decisión crítica</th></tr>
                </thead>
                <tbody>
                  <tr><td>Mecánica y estructura</td><td>Transmitir fuerzas, resistir el ambiente,_mountar los sensores en posición conocida.</td><td>Materiales y grado de protección IP.</td></tr>
                  <tr><td>Actuadores</td><td>Locomoción y manipulación; control de par y posición.</td><td>Redundancia y límites de torque.</td></tr>
                  <tr><td>Percepción</td><td>Cámaras, sensores, LiDAR, IMU; sincronización temporal.</td><td>Qué se procesa a bordo y qué no.</td></tr>
                  <tr><td>Cómputo de a bordo</td><td>Inferencia, control, registro local, control de energía.</td><td>Arquitectura de computadora y del sistema operativo.</td></tr>
                  <tr><td>Telemetría</td><td>Enlace de datos con el operador y con el centro.</td><td>Protocolo, cobertura y comportamiento ante pérdida.</td></tr>
                  <tr><td>Software e interfaz</td><td>Configuración, flujo de inspección, gestión de hallazgos, reportes.</td><td>Modelo de datos: qué se registra y cómo se integra.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>Dónde se pierden los proyectos</p>
              <p>En la interfaz entre el bloque de percepción y el de software. El sensor produce una imagen con metadatos de posición y orientación; el software de inspección necesita saber qué componente es, dónde está y en qué condiciones se tomó. Si ese modelo de datos no se define antes de integrar, la información llega al centro y se pierde.</p>
            </div>
                """,
            },
            {
                "h2": "Cómputo: tres caminos",
                "html": """
            <p>La elección del computador de a bordo define qué se puede hacer en campo durante toda la vida del producto, y por eso conviene tomarla con criterio de largo plazo.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Opción</th><th>Ventajas</th><th>Desventajas</th><th>Cuándo</th></tr>
                </thead>
                <tbody>
                  <tr><td>Placa de consumo (Raspberry Pi y similares)</td><td>Barata,ONSIDERproto rápido, ecosistema amplio.</td><td>Sin rango industrial de temperatura; sin protección; vida útil corta.</td><td>Prototipo de banco y desarrollo de software.</td></tr>
                  <tr><td>Módulo embebido industrial</td><td>Rango térmico amplio, sin disco, Watchdog, ciclo de vida largo.</td><td>Menos potencia de cómputo; ecosistema más limitado.</td><td>Prototipo que va a campo.</td></tr>
                  <tr><td>Controlador industrial (PLC con CPU)</td><td>Determinismo, E/S robustas, ciclo de vida industrial, redundancia.</td><td>Costo, complejidad, y no es un computador de propósito general.</td><td>Producción, cuando el control manda.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-cpu"/></svg>El error de partida</p>
              <p>Arrancar con una placa de consumo y migrar después a hardware industrial. La migración no es solo cambiar la placa: es rehacer el acceso a disco, la gestión térmica, la alimentación y el arranque. Es más barato decidir el hardware de campo desde el primer día, aunque se prototipe sobre una placa de desarrollo.</p>
            </div>
                """,
            },
            {
                "h2": "Telemetría: dimensionarla con números",
                "html": """
            <p>El enlace de datos se subestima siempre y se sobredimensiona a veces. La decisión se toma con el volumen del módulo 04, no con intuición.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Tecnología</th><th>Alcance típico</th><th>Ventaja</th><th>Limitación</th></tr>
                </thead>
                <tbody>
                  <tr><td>Wi-Fi</td><td>Cientos de metros.</td><td>Alto ancho de banda, barato.</td><td>No sirve para línea aérea; punto de acceso por torre.</td></tr>
                  <tr><td>Celular 4G/5G</td><td>Depende de cobertura del operador.</td><td>Cubre el territorio sin infraestructura propia.</td><td>Cobertura irregular en zonas de montaña; costo de datos.</td></tr>
                  <tr><td>IoT celular (LTE-M, NB-IoT)</td><td>Nacional.</td><td>Costo por dato muy bajo, cobertura amplia.</td><td>No sirve para vídeo; solo telemetría.</td></tr>
                  <tr><td>Radio de malla / trunking</td><td>Depende de la topología.</td><td>Cobertura propia, resilient.</td><td>Requiere diseño de red y mantenimiento de torres.</td></tr>
                  <tr><td>Satélite</td><td>Global.</td><td>Cobertura donde no hay nada.</td><td>Costo y latencia; sensible a obstrucciones.</td></tr>
                </tbody>
              </table>
            </div>

            <dl class="glossary">
              <div><dt>Enlace de control</dt><dd>El que lleva órdenes del operador al robot. Necesita baja latencia y debe ser robusto, pero puede ser de bajo ancho de banda.</dd></div>
              <div><dt>Enlace de datos</dt><dd>El que sube capturas y resultados. Necesita ancho de banda, pero tolera más latencia. <strong>Separarlos es la decisión clave</strong> cuando el volumen es alto.</dd></div>
              <div><dt>Almacenamiento local</dt><dd>Registro en tarjeta o disco a bordo para lo que no se puede transmitir. Es la red de seguridad del dato: nada se pierde aunque no haya señal.</dd></div>
            </dl>

            <p>El patrón que funciona: enlace de control robusto y de bajo ancho de banda para operar, enlace de datos separado para subir volumen, y almacenamiento local que se descarga cuando se recupera la señal. Un diseño con un solo enlace suele funcionar en el taller y fallar en la montaña.</p>
                """,
            },
            {
                "h2": "Las tres decisiones caras de revertir",
                "html": """
            <p>En un prototipo hay muchas decisiones, pero solo tres son realmente irreversibles o muy caras de cambiar. Las demás se ajustan en el camino.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Decisión</th><th>Por qué es cara de revertir</th><th>Cómo acertarla</th></tr>
                </thead>
                <tbody>
                  <tr><td>Modelo de datos de los hallazgos</td><td>Si el esquema de registro no contempla lo que la empresa necesita, hay que reprocesar histórico entero.</td><td>Escribir el esquema de datos <em>con el equipo de mantenimiento</em>, no con el de TI, antes de integrar sensores.</td></tr>
                  <tr><td>Interfaz mecánica de los sensores</td><td>El punto de montaje define la geometría de la captura y la repetibilidad de los hallazgos.</td><td>Definirla con la carga útil real de campo, no con la de laboratorio.</td></tr>
                  <tr><td>Estrategia de comunicación</td><td>Determina la cobertura, el costo de datos y el comportamiento en falla.</td><td>Levantar la información de cobertura del tramo antes de elegir, no después.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>La regla del prototipo</p>
              <p>Un primer prototipo no busca ser perfecto, busca <strong>descartar ideas rápido</strong>. Salga a campo pronto, con una sola tarea y un solo tipo de componente, y revise el modelo de datos y la geometría de captura antes de multiplicar sensores. Multiplicar después de validar es barato; cambiar después de multiplicar, no.</p>
            </div>
                """,
            },
        ],
        "taller": {
            "titulo": "Taller: hoja de ruta del prototipo",
            "html": """
            <p>Se construye la hoja de ruta que gobierna el primer prototipo: qué se prueba en cada etapa y cuál es el criterio para pasar a la siguiente. La estructura por etapas evita el error más común, que es intentar construir el producto completo antes de validarlo en campo.</p>
            <ol class="steps">
              <li><strong>Etapa 0 — Mesa.</strong> Modelo de datos y arquitectura de bloques. Salida: el esquema de registro y el diagrama de la interfaz entre bloques.</li>
              <li><strong>Etapa 1 — Banco.</strong> Percepción y computo funcionando con datos reales de la empresa, no con imágenes de internet. Salida: un modelo que clasifica componentes del tramo.</li>
              <li><strong>Etapa 2 — Tienda.</strong> Integración mecánica y eléctrica completa, en el taller, con el prototipo armado. Salida: el sistema encendido y conectado.</li>
              <li><strong>Etapa 3 — Subestación.</strong> Primera salida a un entorno controlado y con operador humano al lado. Salida: una jornada completa con hallazgos registrados.</li>
              <li><strong>Etapa 4 — Línea.</strong> Extensión al activo objetivo, con un solo componente como objetivo. Salida: comparación contra la inspección manual en el mismo tramo.</li>
              <li><strong>Etapa 5 — Repetible.</strong> Segunda y tercera salida sin personal de desarrollo en sitio. Salida: evidencia de que el sistema lo opera alguien del equipo de mantenimiento.</li>
            </ol>
            <p>El criterio de avance entre etapas debe ser un dato, no una opinión: si el prototipo no clasifica bien los componentes del tramo en la etapa 1, ningún ajuste mecánico de la etapa 3 lo va a arreglar.</p>
            """,
            "entrega": (
                "Hoja de ruta de una página: las seis etapas, el entregable de cada una, el criterio de avance "
                "y el recurso estimado por etapa."
            ),
        },
        "resumen_html": """
            <p>Para la gerencia, el mensaje es que <strong>construir el robot es la parte conocida del problema</strong>. Las piezas existen, la ingeniería es estándar y el riesgo técnico está acotado. Lo que no está resuelto son las tres decisiones que no se pueden revertir: el modelo de datos, la interfaz mecánica de captura y la estrategia de comunicaciones.</p>
            <p>Un equipo de desarrollo competente va a acertar la mecánica casi siempre, porque es donde hay menos unknowns. Las tres decisiones que hay que proteger son las de la derecha: son las que cuestan rehacer.</p>
        """,
    },

    # ------------------------------------------------------------------ 10
    {
        "num": "10",
        "titulo": "Proyecto final",
        "lead": (
            "Un proyecto completo, de principio a fin: alcance, plan de validación, "
            "costos, entregables y los criterios para decidir si se escala."
        ),
        "resumen": "Un proyecto real, de principio a fin, validado contra la guía IEC TR 63439-1-2.",
        "icono": "target",
        "meta": [
            ("clock", "120 min de lectura"),
            ("doc", "Módulo 10 de 10"),
            ("target", "Síntesis y plan de proyecto"),
        ],
        "objetivos": [
            "Integrar los nueve módulos anteriores en un plan de proyecto ejecutable.",
            "Definir el alcance de un piloto de forma que tenga un criterio de éxito verificable.",
            "Construir el plan de validación de conformidad con los criterios de la guía aplicable.",
            "Definir los criterios de escalamiento y de detención, antes de empezar.",
        ],
        "secciones": [
            {
                "h2": "El punto de partida",
                "html": """
            <p>Este módulo no introduce conceptos nuevos. Reordena todo lo anterior en una sola pregunta: <strong>dado un activo concreto y un presupuesto concreto, ¿qué proyecto de robótica tiene sentido y cómo se sabe si funcionó?</strong></p>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>El error de la mayoría de los proyectos</p>
              <p>Empezar por la tecnología. "Compremos el robot y veamos qué encontramos." Ese camino produce una demostración impecable y un proyecto sin criterio de éxito, que se evalúa con opiniones y no con datos.</p>
            </div>

            <p>El camino correcto tiene tres líneas de entrada, y las tres tienen que estar resueltas antes de elegir el equipo:</p>
            <ol class="steps">
              <li><strong>El activo y sus modos de falla.</strong> Del módulo 02: qué componentes tienen el historial de hallazgos que justifica la intervención.</li>
              <li><strong>La tarea concreta.</strong> Del módulo 05: un solo escenario, con frecuencia real y criterio de éxito medible.</li>
              <li><strong>El presupuesto y la ventana.</strong> Cuánto se puede invertir y cuántas jornadas al año se pueden gastar en campo.</li>
            </ol>
                """,
            },
            {
                "h2": "Alcance del piloto y criterio de éxito",
                "html": """
            <p>El alcance de un piloto se define por lo que se <em>excluye</em>, no por lo que incluye. Un piloto bien acotado cabe en una frase y tiene un criterio que se puede verificar con un número.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>El piloto incluye</th><th>El piloto NO incluye</th></tr>
                </thead>
                <tbody>
                  <tr><td>Un activo concreto: una subestación o un tramo definido.</td><td>Toda la red. Un piloto no es un programa.</td></tr>
                  <tr><td>Un tipo de componente objetivo, del módulo 02.</td><td>Todos los defectos del activo. Eso es una inspección, no un piloto.</td></tr>
                  <tr><td>Una plataforma, del módulo 03.</td><td>Comparación de plataformas. Eso es una evaluación, no un piloto.</td></tr>
                  <tr><td>Un conjunto de sensores mínimo, del módulo 04.</td><td>Todos los sensores posibles. Añaden costo y ruido.</td></tr>
                  <tr><td>Detección con revisión humana, del módulo 06.</td><td>Intervención física, salvo que el nivel 1 esté ya probado.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>Un criterio de éxito bien escrito</p>
              <p>"En seis jornadas sobre el tramo X, con el robot Y, el sistema detectará al menos el 80% de los defectos que el inspector de referencia identificó, con no más de un falso positivo por torre y con el 100% de los hallazgos georreferenciados."</p>
              <p>Ese criterio tiene activo, número, umbral, comparación contra una referencia y un requisito de evidencia. Es lo que hace que un piloto termine y no se extienda indefinidamente.</p>
            </div>
                """,
            },
            {
                "h2": "Plan de validación",
                "html": """
            <p>La validación responde a una pregunta: ¿cómo vamos a saber que esto funciona? Se organiza en tres capas, con criterios de aceptación explícitos.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Capa</th><th>Qué valida</th><th>Método</th><th>Criterio de aceptación</th></tr>
                </thead>
                <tbody>
                  <tr><td>Funcional</td><td>Que el sistema hace lo que dice hacer.</td><td>Pruebas de laboratorio con piezas de prueba y casos conocidos.</td><td>Detecta los casos conocidos en la proportion definida.</td></tr>
                  <tr><td>Rendimiento</td><td>Que el rendimiento se sostiene en campo.</td><td>Jornadas de campo comparadas contra la inspección de referencia.</td><td>Umbral del criterio de éxito, alcanzado y sostenido.</td></tr>
                  <tr><td>Seguridad y conformidad</td><td>Que se cumplen los requisitos.</td><td>Análisis de riesgo y pruebas de falla, del módulo 08.</td><td>Los riesgos residuales están aceptados y documentados.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-doc"/></svg>Sobre la referencia IEC TR 63439-1-2</p>
              <p>El informe técnico IEC TR 63439-1-2 (2026) es la guía de aplicación que acompaña a la norma de requisitos. Aporta el marco para <strong>cómo demostrar la conformidad</strong> en una evaluación: qué evidencia hay que producir, cómo se documenta y cómo se revisa. Es la referencia que convierte "funciona bien" en "está conforme".</p>
            </div>
                """,
            },
            {
                "h2": "Presupuesto y estructura de costos",
                "html": """
            <p>El presupuesto de un piloto tiene cuatro componentes, y los proveedores suelen cotizar solo el primero. Un presupuesto que solo mira el equipo subestima el proyecto entre un 40% y un 100%.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Componente</th><th>Qué incluye</th><th>Habitualmente omitido</th></tr>
                </thead>
                <tbody>
                  <tr><td>Equipo</td><td>Robot, sensores, plataforma de carga,fta.</td><td>Casi nunca omitido.</td></tr>
                  <tr><td>Software</td><td>Licencias, configuración, integración con los sistemas existentes.</td><td>Frecuentemente, y suele ser la partida más grande en el primer año.</td></tr>
                  <tr><td>Operación</td><td>Tren del operador, despliegue, viáticos, jornadas de campo.</td><td>Se cotiza como si el robot operara solo.</td></tr>
                  <tr><td>Organización</td><td>Capacitación del equipo, procedimientos, revisión de hallazgos.</td><td>Casi nunca está en el presupuesto, y es lo que decide si el sistema se usa.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>La pregunta que revela los presupuestos mal hechos</p>
              <p>"¿Cuántas horas de operador al año, a qué costo, y cuántas horas de revisión de hallazgos?" Si la respuesta viene con dos números y no con un porcentaje, el presupuesto está bien pensado. Si viene con un porcentaje, hay que pedir el desglose.</p>
            </div>
                """,
            },
            {
                "h2": "Escalamiento y criterios de detención",
                "html": """
            <p>Un piloto debería tener definidos, desde el principio, tanto el camino para escalar como las condiciones para detenerse. Lo segundo es lo que casi nunca se escribe, y es lo que protege el proyecto.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Decisión</th><th>Condición</th><th>Qué significa en la práctica</th></tr>
                </thead>
                <tbody>
                  <tr><td>Escalar</td><td>El criterio de éxito se alcanzó en las jornadas de campo y el equipo de operación lo ejecuta sin apoyo externo.</td><td>El sistema es sostenible operativamente.</td></tr>
                  <tr><td>Extender</td><td>El criterio se alcanzó, pero el equipo todavía necesita apoyo de desarrollo.</td><td>Hace falta más capacitación antes de crecer; no es un fracaso.</td></tr>
                  <tr><td>Ajustar</td><td>El criterio se alcanzó solo parcialmente y la causa es conocida y corregible.</td><td>Se itera con un cambio acotado, no con un proyecto nuevo.</td></tr>
                  <tr><td>Detener</td><td>El criterio no se alcanza por una causa que no depende del ajuste, o el riesgo residual no es aceptable.</td><td>Se documenta lo aprendido y se cierra. Esto también es un resultado.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout callout-warn">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-shield"/></svg>Sobre la presión de escalar</p>
              <p>Un piloto que "funcionó bien" pero que el equipo de operación no puede operar sin el proveedor no escaló: se convirtió en una consultoría permanente. La prueba real de que un proyecto de robótica funciona es si sobrevive al fin del contrato de desarrollo.</p>
            </div>
                """,
            },
        ],
        "taller": {
            "titulo": "Taller: propuesta final de proyecto",
            "html": """
            <p>La demostración final del curso: una propuesta de proyecto completa, en un documento de tres páginas, que un comité pueda aprobar o rechazar con los elementos que tiene a la vista.</p>
            <ol class="steps">
              <li><strong>Página 1 — El problema.</strong> Activo, componentes con historial, tarea prioritaria y por qué es un problema y no una mejora.</li>
              <li><strong>Página 2 — La solución y el alcance.</strong> Plataforma y sensores elegidos, con la justificación de los módulos 03 y 04; qué incluye el piloto y qué NO, según la tabla del módulo.</li>
              <li><strong>Página 3 — Validación, presupuesto y decisión.</strong> Criterio de éxito medible, plan de validación de tres capas, presupuesto en las cuatro partidas, y la tabla de escalamiento y detención.</li>
            </ol>
            <p>Antes de entregarla, revise tres cosas: ¿el criterio de éxito tiene un número?; ¿el presupuesto tiene las cuatro partidas?; ¿existe una condición de detención? Si las tres respuestas son sí, la propuesta está lista para un comité.</p>
            """,
            "entrega": (
                "Propuesta de proyecto de tres páginas: problema, solución y alcance, validación, presupuesto "
                "y criterios de escalamiento y detención."
            ),
        },
        "resumen_html": """
            <p>Para cerrar el curso, la idea que resume los diez módulos es esta: <strong>la robótica de red es una disciplina de ingeniería de decisión antes que de ingeniería de hardware</strong>. Las máquinas se Comparan, se eligen y se compran. El proyecto lo define una organización que sabe qué falla en su activo, qué puede pagar y qué evidencia necesita para decidir.</p>
            <p>Quien entienda eso puede evaluar cualquier propuesta de provider que se le presente: no por lo que promete hacer el robot, sino por cómo propone medir su propio desempeño y qué pasa si no lo alcanza. Ese es el criterio, y es el único que escala.</p>
            <p><strong>Buen curso, y buen uso de los robots.</strong></p>
        """,
    },
]
