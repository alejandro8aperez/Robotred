"""Modulos 05 a 10 del curso.

Se separa del bloque 01-04 solo para mantener archivos manejables en el
editor; _curso_datos.py los importa y los concatena a MODULOS.
"""

MODULOS_B = [
    # ------------------------------------------------------------------ 05
    {
        "num": "05",
        "titulo": "Qué puede hacer ROBOTY-RED",
        "lead": (
            "Capacidades operativas reales, el alcance honesto de la plataforma y "
            "los escenarios donde un robot de mantenimiento cambia el resultado."
        ),
        "resumen": "Capacidades operativas, alcance real y escenarios de aplicación en campo.",
        "icono": "wrench",
        "meta": [
            ("clock", "90 min de lectura"),
            ("doc", "Módulo 5 de 10"),
            ("wrench", "Del diagnóstico a la intervención"),
        ],
        "objetivos": [
            "Distinguir entre lo que la plataforma puede hacer hoy y lo que está en desarrollo.",
            "Enmarcar un escenario de aplicación en términos de tarea, activo y evidencia esperada.",
            "Construir el caso de negocio de un piloto con costos y ahorro explícitos.",
            "Reconocer los cuatro límites que aparecen en cualquier propuesta comercial.",
        ],
        "secciones": [
            {
                "h2": "Las tres capacidades, en orden de madurez",
                "html": """
            <p>Conviene presentar las capacidades en orden, no en permanente: la diferencia entre lo que ya opera y lo que se está desarrollando es la que separa una propuesta seria de una promesa.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Capacidad</th><th>Estado</th><th>Qué resuelve</th><th>Qué no resuelve</th></tr>
                </thead>
                <tbody>
                  <tr><td>Inspeccióntermográfica</td><td>Operativa</td><td>Puntos calientes en conexiones, herrajes y bushings, con punto de referencia medido.</td><td>No mide lo que no está expuesto ni corrige lo que encuentra.</td></tr>
                  <tr><td>Inspección visual</td><td>Operativa</td><td>Corrosión, deformación, ausencia de pernos, condición de aisladores, con evidencia georreferenciada.</td><td>No distingue un defecto activo de uno inactivo sin medición adicional.</td></tr>
                  <tr><td>Detección de descargas parciales</td><td>Operativa</td><td>Corona y descarga superficial en aislamiento, audible y ultrasónica.</td><td>No localiza con precisión cuando hay varios puntos activos en la misma estructura.</td></tr>
                  <tr><td>Georreferenciación de hallazgos</td><td>Operativa</td><td>Cada registro queda associado a torre, componente y orientación.</td><td>No reemplaza el criterio del inspector en la clasificación de severidad.</td></tr>
                  <tr><td>Limpieza de aisladores</td><td>En desarrollo</td><td>Reducir la contaminación sin desconectar el conductor.</td><td>No sustituye la substituição en porcelana defectuosa.</td></tr>
                  <tr><td>Intervención: apriete y cambio</td><td>En desarrollo</td><td>Cerrar el ciclo sin cortar el servicio de la línea.</td><td>Requiere procedimiento, herramienta y trazabilidad propios.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>La honestidad es un argumento de venta</p>
              <p>Un proveedor que dice qué <em>no</em> hace genera más confianza que uno que dice que lo hace todo. En esta industria, la primera pregunta de un comité técnico no es qué hace su robot, sino qué le falla cuando se moja.</p>
            </div>
                """,
            },
            {
                "h2": "Cuatro límites que aparecen en toda propuesta",
                "html": """
            <p>Estos cuatro puntos son los que separan un presupuesto de un caso de negocio. Si faltan en la propuesta, el proyecto se.profile problematico antes de empezar.</p>

            <h3>El límite del clima</h3>
            <p>Ninguna plataforma funciona con viento por encima de su umbral. Eso no es una falla del equipo, es una restricción del activo. La propuesta debe decir qué pasa en una semana de rachas: ¿se cancela la jornada, se cambia a otra tarea, o se pierde el día?</p>

            <h3>El límite del operador</h3>
            <p>Todo robot de red necesita un operador competente: alguien que sepa interpretar lo que ve y que decida cuándo detener la operación. Si la propuesta asume que el robot es autónomo de extremo a extremo, o bien no entiende el producto, o bien está vendiendo una expectativa que el equipo no puede sostener.</p>

            <h3>El límite de la ventana de trabajo</h3>
            <p>Una torre se inspecciona en una hora y se desplaza en otra. El tiempo real por punto es mucho mayor que el tiempo de captura. Cualquier caso de negocio que calcule horas de robot sin horas de desplazamiento se va a quedar corto por un factor de dos o tres.</p>

            <h3>El límite del dato</h3>
            <p>El robot produce hallazgos, no decisiones. Alguien tiene que revisar, clasificar y ordenar el trabajo. Ese costo de recurso humano existe siempre y rara vez aparece en el presupuesto de la propuesta.</p>

            <div class="callout callout-warn">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-shield"/></svg>Advertencia de procurement</p>
              <p>Cuando una propuesta presenta un "ahorro de 40%" y no desglosa horas de robot, horas de operador, ni costo de revisión de hallazgos, ese 40% incluye un supuesto que no se va a cumplir. Pida el desglose antes de comparar.</p>
            </div>
                """,
            },
            {
                "h2": "Escenarios con retorno comprobado",
                "html": """
            <p>No todos los escenarios son iguales. Estos son los que han demostrado retorno en operación real, ordenados por dificultad de entrada.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Escenario</th><th>Frecuencia</th><th>Valor principal</th><th>Dificultad</th></tr>
                </thead>
                <tbody>
                  <tr><td>Termografía en subestación</td><td>Ronda programada mensual.</td><td>Detección temprana de puntos calientes en conexiones.</td><td>Baja: recinto cerrado, vehicle access.</td></tr>
                  <tr><td>Inspección visual de herrajes en línea</td><td>Ronda anual o semestral.</td><td>Priorización objetiva del mantenimiento correctivo.</td><td>Media: requiere plataforma trepadora o dron.</td></tr>
                  <tr><td>Detección de corona en aisladores</td><td>Ronda específica en temporada seca o contaminada.</td><td>Hallazgo de defecto activo antes de la falla.</td><td>Media: condicionada por clima y hora del día.</td></tr>
                  <tr><td>Inspección tras evento</td><td>Después de tormenta, quake o trabajo de terceros.</td><td>Evaluación rápida sin exponer personal a la estructura dañada.</td><td>Media-alta: la estructura puede estar inestable.</td></tr>
                  <tr><td>Intervención de emergencia</td><td>Reactiva.</td><td>Restablecimiento de servicio sin línea de.diablillo temporal.</td><td>Alta: requiere intervención probada y equipo de respaldo.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>Dónde empezar</p>
              <p>El primer escenario de cualquier programa debe ser de baja dificultad y alta frecuencia. La subestación cumple las dos condiciones. El retorno no será el más alto del catálogo, pero es el que permite aprender la operación, formir al equipo y construir el historial que después justifica el escalamiento a línea.</p>
            </div>
                """,
            },
            {
                "h2": "El argumento de costo total de propiedad",
                "html": """
            <p>Un robot de red no se compara con el costo de una inspección manual, sino con el costo de mantener el recurso humano que la hace, más el riesgo que se elimina.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Componente</th><th>Inspección manual</th><th>Inspección robótica</th><th>Nota</th></tr>
                </thead>
                <tbody>
                  <tr><td>Equipo humano en sitio</td><td>Cuadrilla de 2 personas por jornada.</td><td>1 operador (+ cuadrilla de apoyo en despliegue).</td><td>La diferencia es menor de lo que parece: el operador sigue ahí.</td></tr>
                  <tr><td>Exposición a riesgo</td><td>Alta: altura, arco eléctrico, caída.</td><td>Baja: el operador permanece en tierra.</td><td>Es el argumento más sólido y el menos cuantificado.</td></tr>
                  <tr><td>Consistencia de datos</td><td>Variable según operario y momento.</td><td>Uniforme y comparable entre años.</td><td>Permite seguir la evolución de un defecto.</td></tr>
                  <tr><td>Evidencia</td><td>Notas y fotos sin georreferencia.</td><td>Registro estructurado por componente.</td><td>Reduceiapartados de los discussions de prioridad.</td></tr>
                  <tr><td>Tiempo de ciclo</td><td>Limitado por clima y luz del día.</td><td>Similar o mejor; ampliable con iluminación propia.</td><td>Depende del tipo de plataforma.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>El argumento que sostiene el proyecto</p>
              <p>El retorno más defendible de un robot de red no es el ahorro de horas de mano de obra: es la <strong>reducción de exposición al riesgo</strong> y la <strong>consistencia del dato</strong>. El primer argumento es difícil de cotizar, y el segundo es el que permite capturar el valor real del activo.</p>
            </div>
                """,
            },
        ],
        "taller": {
            "titulo": "Taller: caso de negocio de un piloto",
            "html": """
            <p>Se construye el caso de negocio completo de un escenario, con los números que un comité pediría. La diferencia entre este taller y una hoja de cálculo es que todo supuesto debe quedar escrito y visible.</p>
            <ol class="steps">
              <li><strong>Describa el escenario en una frase</strong> con activo, tarea y frecuencia real.</li>
              <li><strong>Estime el costo actual</strong> de esa tarea por año: jornadas, personas, viáticos, equipos y tiempo de exposures.</li>
              <li><strong>Estime el costo del piloto</strong>: equipo, operador, despliegue, software e integración de datos.</li>
              <li><strong>Calcule el tiempo real por punto</strong> incluyendo desplazamiento, montaje y desmontaje, no solo captura.</li>
              <li><strong>Estime los hallazgos esperados</strong> a partir del histórico del Módulo 02, y qué fracción evita trabajo correctivo.</li>
              <li><strong>Escriba el supuesto más frágil</strong> y qué haría que el proyecto se detenga.</li>
            </ol>
            <p>El paso 6 es el que más valor tiene para el proyecto. Un caso de negocio sin criterio de detención definido es un documento de promoción, no un plan.</p>
            """,
            "entrega": (
                "Caso de negocio de una página con costos actuales, costos del piloto, tiempo por punto, "
                "hallazgos esperados y el criterio de detención del proyecto."
            ),
        },
        "resumen_html": """
            <p>Para la gerencia, el mensaje de este módulo es que <strong>ROBOTY-RED no reemplaza al equipo de mantenimiento: lo reubica en la tarea que aporta valor</strong>. El operador deja de subir a estructuras y pasa a interpretar evidencia y a decidir prioridades.</p>
            <p>Ese cambio es cultural antes que técnico. Un programa de robótica de red que no incluya al equipo de operación en el diseño del procedimiento no va a ser adoptado, por bueno que sea el equipo. La tecnología es la parte fácil.</p>
        """,
    },

    # ------------------------------------------------------------------ 06
    {
        "num": "06",
        "titulo": "Inteligencia artificial y procesamiento en el borde",
        "lead": (
            "Por qué el robot decide en campo en lugar de enviar vídeo a la nube, y "
            "cómo diseñar un sistema de detección que un inspector pueda auditar."
        ),
        "resumen": "Cómo el robot decide en campo en lugar de enviar vídeo crudo a la nube.",
        "icono": "ai",
        "meta": [
            ("clock", "90 min de lectura"),
            ("doc", "Módulo 6 de 10"),
            ("ai", "Percepción y decisión en campo"),
        ],
        "objetivos": [
            "Explicar las cuatro razones por las que el procesamiento va en el robot y no en el centro de datos.",
            "Distinguir un sistema de detección clásico de uno basado en aprendizaje profundo, en el contexto de inspección eléctrica.",
            "Dimensionar un presupuesto de cómputo en borde realista.",
            "Definir el papel del humano en el bucle de decisión, y por qué no puede eliminarse.",
        ],
        "secciones": [
            {
                "h2": "Por qué el procesamiento va en el borde",
                "html": """
            <p>La decisión de dónde se procesa el vídeo no es una preferencia técnica: es la que determina si el sistema funciona en el mundo real o solo en la demostración.</p>

            <ol class="steps">
              <li><strong>Ancho de banda.</strong> Una hora de vídeo de inspección de una torre ocupa cientos de megabytes. Multiplicado por diez torres por jornada y por un corredor completo, la transmisión se vuelve el cuello de botella, y en campo cellular la cobertura no está garantizada.</li>
              <li><strong>Latencia.</strong> Un hallazgo que se detecta a distancia y que la IA confirma en dos segundos sirve. El mismo hallazgo con ida y vuelta a un centro de datos a 300 km ya llegó tarde para que el operador actúe sobre esa torre en esa jornada.</li>
              <li><strong>Disponibilidad.</strong> El campo no tiene señal. Un sistema que depende de la nube no puede usarse en el lugar donde el problema está.</li>
              <li><strong>Privacidad y custodia.</strong> La infraestructura crítica es un objetivo. Procesar localmente significa que el dato sensible nunca sale del perímetro controlado.</li>
            </ol>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>El patrón correcto</p>
              <p><strong>En el borde</strong>, el robot filtra, detecta y prioriza. <strong>En el centro de datos</strong>, se archivan los hallazgos, se entrenan modelos con el histórico y se construyen reportes. No es "todo local" ni "todo en la nube": es cada tarea donde le conviene.</p>
            </div>
                """,
            },
            {
                "h2": "Qué debe decidir el robot, en concreto",
                "html": """
            <p>La palabra "IA" en una propuesta de inspección evoke demasiado. Las decisiones concretas que un robot debe tomar en campo son mucho más acotadas, y por eso son implementables.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Decisión</th><th>Qué resuelve</th><th>Complejidad</th></tr>
                </thead>
                <tbody>
                  <tr><td>¿La imagen estátomada?</td><td>Descarta fotos borrosas o mal iluminadas y vuelve a capturar.</td><td>Baja: reglas deumbrales.</td></tr>
                  <tr><td>¿Hay algo ahí?</td><td>Detecta presencia de un componente en la escena esperada.</td><td>Media: detección de objetos.</td></tr>
                  <tr><td>¿Qué es?</td><td>Clasifica: aislador, grapa, conector, conductor, estructura.</td><td>Media-alta: clasificación entrenada.</td></tr>
                  <tr><td>¿Es grave?</td><td>Prioriza: separa lo que requiere intervención de lo que no.</td><td>Alta y delicada: es donde entra el criterio del inspector.</td></tr>
                  <tr><td>¿Seguimos?</td><td>Modifica la ruta de inspección según lo encontrado: más tomas si hay defecto, menos si no.</td><td>Media: lógica de decisión sobre los anteriores.</td></tr>
                </tbody>
              </table>
            </div>

            <p>Obsérvese que ninguna de estas decisiones requiere que el robot "entienda" la red eléctrica. Requiere que clasifique correctamente lo que ve. Esta distinción es la que separa un proyecto de inspección viable de una promesa de autonomía total.</p>

            <div class="callout">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-doc"/></svg>Advertencia</p>
              <p>Cualquier propuesta que describa el sistema como "IA que entiende la línea eléctrica" está describiendo algo que no existe en producción. Lo que existe es clasificación de componentes y priorización con supervisión humana.</p>
            </div>
                """,
            },
            {
                "h2": "Cómputo en borde: qué se puede y qué no se puede",
                "html": """
            <p>El robot tiene un presupuesto de cómputo de quelques..

            watts, y eso define lo que es realista ejecutar localmente.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Tarea</th><th>Cómputo típico</th><th>¿En borde?</th></tr>
                </thead>
                <tbody>
                  <tr><td>Control de movimiento y servo</td><td>Determinista, ciclos de milisegundos.</td><td>Obligatoriamente en borde.</td></tr>
                  <tr><td>Detección de objetos (YOLO-clase)</td><td>Unos pocos gigaflops, viable con GPU de bajo consumo o NPU.</td><td>Sí, con hardware adecuado.</td></tr>
                  <tr><td>Segmentación de defectos</td><td>Más costosa que la detección; requiere modelo optimizado.</td><td>Posible, con cuantización.</td></tr>
                  <tr><td>Clasificación de imágenes (ResNet / ViT pequeño)</td><td>Moderada.</td><td>Sí.</td></tr>
                  <tr><td>Entrenamiento y reentrenamiento de modelos</td><td>Horas de GPU.</td><td>Nunca en el robot.</td></tr>
              <tr><td>Modelo de lenguaje para reportes</td><td>Decenas de miles de millones de parámetros.</td><td>No. En el centro de datos.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>La técnica que hace viable el borde</p>
              <p><strong>Cuantización</strong>: reducir la precisión de los pesos del modelo —de 32 bits a 8— multiplica la velocidad de inferencia y reduce el consumo de memoria, con una pérdida deExactitud mínima. Es lo que permite correr un detector de defectos decente en un_processor de un brazo robótico, sin tarjeta gráfica dedicada.</p>
            </div>
                """,
            },
            {
                "h2": "Falsos positivos y el costo invisible",
                "html": """
            <p>Un sistema de inspección se juzga por dos números: cuántos defectos reales encuentra y cuántos falsos positivos produce. La industria haAGON se ha enfocado en el primero y ha subestimado el segundo, que es el que determina si el sistema se usa.</p>

            <ul class="bullets">
              <li><strong>Un falso positivo</strong> no es gratis: alguien tiene que revisar el hallazgo, decidir que no es nada y descartarlo. Con cientos de hallazgos por jornada, esto consume días de trabajo de inspección.</li>
              <li><strong>Un falso negativo</strong> es un defecto real que pasa. Es el error grave, pero es el menos frecuente si el modelo se ajusta a ser conservador.</li>
              <li><strong>La consecuencia del error bajo</strong> es la rechazo del sistema: si el inspector ve que el 30% de las alertas son ruido, deja de mirar las alertas.</li>
            </ul>

            <div class="callout callout-warn">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-shield"/></svg>La decisión de umbral que hay que hacer explícita</p>
              <p>Todo detector tiene un umbral de confianza que decide qué se reporta. Subirlo reduce falsos positivos y aumenta falsos negativos. <strong>Ese umbral es una decisión de política de mantenimiento, no una decisión técnica:</strong> lo debe tomar la empresa, no el proveedor, y debe quedar escrito.</p>
            </div>
                """,
            },
            {
                "h2": "El humano en el bucle",
                "html": """
            <p>La supervisión humana no es un freno a la autonomía: es lo que hace que el sistema sea responsable. El robot prioriza; el inspector valida y decide.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Nivel de automatización</th><th>Qué hace el robot</th><th>Qué hace el inspector</th><th>Riesgo</th></tr>
                </thead>
                <tbody>
                  <tr><td>Asistido</td><td>Captura y ordena.</td><td>Revisa todo y clasifica.</td><td>Bajo: el sistema nunca prioriza solo.</td></tr>
                  <tr><td>Supervisado</td><td>Prioriza y propone la acción.</td><td>Valida, corrige o descarta.</td><td>Medio: requiere auditoría de las decisiones del modelo.</td></tr>
                  <tr><td>Autónomo</td><td>Decide y ejecuta la intervención.</td><td>Supervisa excepciones.</td><td>Alto: solo con marco normativo y casos de prueba extensos.</td></tr>
                </tbody>
              </table>
            </div>

            <p>El sector eléctrico rara vez necesita el tercer nivel, y casi siempre empieza en el primero. Ese es un rasgo de la industria, no una limitación del robot: cuando el error se mide en un blackout, la confianza se gana nivel por nivel.</p>
                """,
            },
        ],
        "taller": {
            "titulo": "Taller: definir el conjunto de datos de un tramo",
            "html": """
            <p>Si el proyecto va a usar aprendizaje automático, el conjunto de datos es el activo más valioso y el más difícil de conseguir. Este taller produce el plan para construirlo.</p>
            <ol class="steps">
              <li><strong>Recopile el histórico</strong> de hallazgos de los últimos años: fotos, reportes, órdenes de trabajo.</li>
              <li><strong>Clasifique</strong> cada imagen según el tipo de componente y si contiene defecto, con etiquetas consistentes.</li>
              <li><strong>Cuantifique el desbalance</strong>: lo más común es que el 95% de las imágenes no tenga defecto y el 5% sí. Anote el número real.</li>
              <li><strong>Separe los conjuntos</strong> de entrenamiento y de prueba <em>por estructura, no al azar</em>, para que el rendimiento mida capacidad de generalizar y no de memorizar.</li>
              <li><strong>Defina el umbral de confianza inicial</strong> y escríbalo, con el criterio de negocio que lo justifica.</li>
              <li><strong>Defina el protocolo de revisión</strong> humana: quién revisa, en cuánto tiempo y cómo se registra.</li>
            </ol>
            <p>El error más común en proyectos de IA es evaluar el modelo con imágenes del mismo tipo de estructura que se usó para entrenar, y obtener un número excelente que después se degrada en campo. El paso 4 es el que evita esa trampa.</p>
            """,
            "entrega": (
                "Plan de construcción del conjunto de datos: fuentes, esquema de etiquetas, cuantificación de "
                "desbalance, criterio de separación por estructura y protocolo de revisión humana."
            ),
        },
        "resumen_html": """
            <p>Para la gerencia, el mensaje es que <strong>la inteligencia artificial en un robot de red no es una promesa de autonomía total</strong>: es un filtro que reduce el volumen de datos que llega a un inspector y le entrega lo importante primero.</p>
            <p>Eso tiene un beneficio directo y medible: si hoy un inspector revisa 400 imágenes por jornada y solo 30 tienen algo interesante, el valor de la IA es que revise esas 400 en segundos y le muestre las 30. El resto de la propuesta —nube, entrenamiento continuo, gemelo digital— es infraestructura para que eso escale, no el producto en sí.</p>
        """,
    },
]