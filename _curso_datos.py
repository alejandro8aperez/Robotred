"""Contenido del curso ROBOTY-RED.

Cada entrada de MODULOS genera una pagina en curso/modulo-NN.html.
El HTML de las secciones va completo para poder usar tablas, avisos y
listas de glosario sin inventar sintaxis nueva en el generador.

Campos por modulo
  num      numero de pagina, "01" .. "10"
  titulo   titulo visible (tambien va en el <title>)
  lead     frase de apertura, se usa como meta description
  resumen  linea corta para el indice
  icono    id de icono en _gen_curso.ICONOS
  meta     [(icono, texto), ...] bajo el titulo
  objetivos  lista de "<li>"
  secciones  [{"h2": ..., "html": ...}, ...]
  taller   {"titulo", "html", "entrega"} opcional
  resumen_html  HTML del bloque "Resumen para la gerencia"
"""

CURSO = {
    "titulo": "Curso de robótica para redes eléctricas — 10 módulos",
    "descripcion": (
        "Contenido completo del curso de ROBOTY-RED: 10 módulos sobre robótica "
        "aplicada al mantenimiento de líneas de transmisión y distribución, "
        "desde la terminología IEC 63439-1-1 hasta el diseño de prototipos y "
        "el proyecto final."
    ),
    "lead": (
        "Ruta de aprendizaje para gerencia, gestión de activos y líderes de "
        "mantenimiento de empresas del sector eléctrico. Diez módulos en español "
        "que avanzan desde el marco normativo internacional hasta el diseño y la "
        "validación de un primer prototipo."
    ),
    "meta": [
        ("clock", "10 módulos · ~90 min de lectura por módulo"),
        ("doc", "En español, con referencias normativas"),
        ("target", "Caso real: Spot en National Grid"),
        ("layers", "Nivel: profesional"),
    ],
    "antes_p1": (
        "Este curso no enseña a programar un robot. Enseña a <strong>decidir, "
        "especificar y supervisar</strong> robots que trabajan en redes eléctricas: "
        "qué resuelven, bajo qué norma se regulan, cuánto cuestan y qué ocurre "
        "cuando fallan."
    ),
    "antes_p2": (
        "El material se apoya en el trabajo del Comité Técnico 129 de la Comisión "
        "Electrotécnica Internacional (IEC/TC 129) y en despliegues reales de "
        "industria. Las referencias normativas se citan con fines formativos; "
        "para una decisión de compra o una demostración debe consultarse el texto "
        "vigente y la normativa local aplicable."
    ),
    "regla_titulo": "Regla de oro del curso",
    "regla": (
        "Ninguna plataforma robótica sustituye a los procedimientos de seguridad de "
        "su compañía. La autonomía cambia <em>quién ejecuta</em> la tarea y "
        "<em>con qué evidencia</em> se registra, nunca <em>bajo qué reglas</em> se ejecuta."
    ),
    "programa_h2": "El programa",
    "cierre_h2": "Para qué sirve todo esto",
    "cierre_p1": (
        "Al terminar el curso se debería poder: leer una especificación técnica de un "
        "robot de red sin depender del proveedor; definir qué plataforma conviene para "
        "un tramo concreto; evaluar una propuesta comercial contra criterios técnicos; "
        "y establecer qué evidencia un piloto debe entregar para justificar el escalamiento."
    ),
    "cierre_fuerte": "Ese es el objetivo: que la decisión de robotizar una red se tome con argumentos, no con entusiasmo.",
}

MODULOS = [
    # ------------------------------------------------------------------ 01
    {
        "num": "01",
        "titulo": "Introducción a la robótica eléctrica",
        "lead": (
            "Qué es un robot de energía eléctrica, por qué el sector eléctrico fue "
            "el primero en estandarizarlo y qué cambia realmente cuando un robot "
            "sube a una torre."
        ),
        "resumen": "Qué es un robot de energía eléctrica y por qué este sector fue el primero en estandarizarlo.",
        "icono": "robo",
        "meta": [
            ("clock", "90 min de lectura"),
            ("doc", "Módulo 1 de 10"),
            ("shield", "Base normativa y de seguridad"),
        ],
        "objetivos": [
            "Distinguir una plataforma de inspección de una de intervención, y por qué la diferencia cambia el proyecto entero.",
            "Explicar por qué el sector eléctrico necesitaba un estándar propio y no pudo quedarse con la robótica industrial tradicional.",
            "Reconocer los cuatro límites que ningún robot de red puede cruzar: tensión, peso, clima y responsabilidad legal.",
            "Leer el índice de la norma IEC 63439-1-1 y saber qué parte de cada requisito le toca al proveedor y cuál al usuario.",
        ],
        "secciones": [
            {
                "h2": "Por qué el eléctrico fue el primer sector en estandarizar robots",
                "html": """
            <p>La robótica industrial maduró alrededor de una fábrica: volumen definido, pallets, procesos repetitivos, ambiente controlado. El robot industrial asume que el piso está limpio, que hay luz, que nadie se acerca y que la máquina-danger está detrás de una barrera.</p>
            <p>Una torre de transmisión no cumple ninguna de esas condiciones. El trabajo se hace a veinte metros de altura, con viento, a cuatro mil metros sobre el nivel del mar si toca, sobre una estructura de acero galvanizado que cambia de forma con el sol, y a metros de un conductor que puede estar a 138 kV aunque el tramo esté desenergizado en ese momento.</p>
            <p>Esa diferencia explica por qué el Comité Técnico 129 de la IEC homem un grupo de trabajo específico para <em>robots para inspección y mantenimiento de líneas aéreas de alta tensión</em>. No es un caso de uso más de la robótica: es una familia técnica con sus propios riesgos, sus propios ensayos y su propia documentación.</p>

            <div class="callout">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-shield"/></svg>Punto clave</p>
              <p>Un robot industrial que funciona bien en una planta puede ser perfectamente inaceptable en una línea aérea, y no por culpa de sus motores: sino porque sus <strong>supuestos de seguridad</strong> no se cumplen.</p>
            </div>
                """,
            },
            {
                "h2": "Las tres generaciones de robot de red",
                "html": """
            <p>Casi todo el marketing del sector se puede ordenar en tres etapas. Entender en cuál está su proyecto evita comprar tecnología de la etapa equivocada.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Generación</th><th>Qué hace</th><th>Qué exige del usuario</th><th>Madurez</th></tr>
                </thead>
                <tbody>
                  <tr><td>1. Sensorial</td><td>Recorre y captura: fotos, vídeo, termografía, LiDAR.</td><td>Casi nada: un operador y una plataforma de datos.</td><td>Alta, comercial desde hace más de una década.</td></tr>
                  <tr><td>2>Diagnóstico</td><td>Interpreta en campo y prioriza: separa lo grave de lo cosmético.</td><td>Un criterio de inspección y un proceso de revisión.</td><td>Media, en Depends de la calidad del modelo.</td></tr>
                  <tr><td>3. Intervención</td><td>Actúa: limpia, aprieta, cambia un componente, manipula.</td><td>Procedimiento, herramienta y trazabilidad.</td><td>Baja, y por eso es la que más valor tiene.</td></tr>
                </tbody>
              </table>
            </div>

            <p>El salto de la primera a la segunda generación es de software. El salto de la segunda a la tercera es de seguridad, y por eso se mueve más despacio y se exige con más requisitos de certificación.</p>
                """,
            },
            {
                "h2": "El caso de referencia: Spot en la red de National Grid",
                "html": """
            <p>En el Reino Unido, National Grid fue de los primeros operadores de redes en llevar robots cuadrúpedos de Boston Dynamics a inspección de subestaciones y de líneas aéreas, yHa usado esa experiencia como argumento comercial durante años. El caso se cita mucho, y con razón: fue de los primeros casos <em>comerciales</em> y no solo de laboratorio de un robot cuadrúpedo trabajando en infraestructura crítica.</p>
            <p>Lo que el caso demuestra, en orden de importancia:</p>
            <ul class="bullets">
              <li>Que un robot comercial de propósito general puede foothold en una subestación sin pantalla propia.</li>
              <li>Que la barrera no era la tecnología del robot sino el <strong>proceso de integración</strong> con los sistemas del operador.</li>
              <li>Que el valor estaba en la evidencia, no en el movimiento: cada hora de video ordenaba la cola de mantenimiento.</li>
            </ul>

            <div class="callout callout-warn">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-doc"/></svg>Sobre las fuentes</p>
              <p>Los detalles del caso (fechas, alcance, cifras de rendimiento) cambiaron varias veces entre comunicados de prensa y publicaciones técnicas. Si va a citarlo en una presentación corporativa, verifíquelo contra la fuente original vigente; este módulo lo usa como <strong>referencia conceptual</strong>, no como fuente de cifras.</p>
            </div>
                """,
            },
            {
                "h2": "Qué es y qué no es un robot de red",
                "html": """
            <p>Conviene fijar el vocabulario antes de discutir tecnología, porque buena parte de las malas compras vienen de esperar capacidades que pertenecen a otra categoría de producto.</p>

            <dl class="glossary">
              <div><dt>Robot de inspección</dt><dd>Plataforma que se aproxima al activo y recoge datos. No modifica el activo. Es la categoría más madura y la de menor riesgo regulatorio.</dd></div>
              <div><dt>Robot de intervención</dt><dd>Plataforma que ejecuta una acción física sobre el activo: limpieza, apriete, remplacement de un componente. Entra en el territorio de la seguridad eléctrica y de la responsabilidad de calidad.</dd></div>
              <div><dt>Plataforma de movilidad</dt><dd>El medio de locomoción: drone, UGV, trepador, UUV, hybrid. No define la capacidad; la define lo que lleva montado encima.</dd></div>
              <div><dt>Carga útil (payload)</dt><dd>Masa máxima que la plataforma puede transportar además de sí misma y de su batería. Es la cifra que decide si un robot sirve para su tarea.</dd></div>
              <div><dt>Sistema robótico de línea</dt><dd>El conjunto completo: plataforma, carga útil, comunicaciones, software, operador y procedimiento. Es lo que se certifica y lo que se compra, no la plataforma.</dd></div>
            </dl>
                """,
            },
            {
                "h2": "El marco normativo: qué esperar de IEC/TC 129",
                "html": """
            <p>El Comité Técnico 129 de la IEC trabaja en la familia de normas sobre robots para inspección y mantenimiento de líneas aéreas de alta tensión. Dos documentos son la referencia habitual al especificar un proyecto:</p>
            <ul class="bullets">
              <li><strong>IEC 63439-1-1</strong>, publicada en 2025, es la norma de requisitos: define qué debe cumplir un robot de este tipo, con Emphasis en seguridad, en condiciones de entorno severas y en la cadena de información.</li>
              <li><strong>IEC TR 63439-1-2</strong>, el informe técnico de 2026, aporta orientación y guía de aplicación: cómo interpretar los requisitos en la práctica y cómo demostrar la conformidad en una evaluación.</li>
            </ul>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>Cómo usarlas</p>
              <p>La <strong>norma</strong> sirve para <em>exigir</em>: es la lista de requisitos que va en el pliego. El <strong>informe técnico</strong> sirve para <em>interpretar</em>: es la guía que evita que dos proveedores interpreten el mismo requisito de forma distinta. Pedir únicamente un certificado de cumplimiento de la norma, sin página, es pedir poco.</p>
            </div>

            <p>La norma no sustituye a la normativa eléctrica local. Define el comportamiento del robot; la seguridad del trabajo la define el operador según su propia regulación y sus propios procedimientos.</p>
                """,
            },
            {
                "h2": "Cómo leer una especificación de un robot de red",
                "html": """
            <p>Las fichas técnicas de estos equipos están escritas para impresionar, no para decidir. Estos son los seis bloques que hay que buscar y los cinco números que hay que exigir.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Bloque de la ficha</th><th>Lo que promete</th><th>La pregunta que lo desarma</th></tr>
                </thead>
                <tbody>
                  <tr><td>Alcance operativo</td><td>"hasta 40 m de altura"</td><td>¿En qué temperatura, con qué viento y sobre qué superficie?</td></tr>
                  <tr><td>Autonomía</td><td>"8 horas de operación"</td><td>¿Con qué payload y a qué temperatura? La cifra sin payload no significa nada.</td></tr>
                  <tr><td>Inspección</td><td>"termografía y visión de alta resolución"</td><td>¿A qué distancia, con qué emisividad y con qué tolerancia?</td></tr>
                  <tr><td>Seguridad</td><td>"diseño redundante"</td><td>¿Redundancia de qué exactamente? ¿Qué pasa si falla el enlace?</td></tr>
                  <tr><td>Certificaciones</td><td>"IEC 63439, CE, IP67"</td><td>¿Certificado por entidad externa o autodeclaración del fabricante?</td></tr>
                  <tr><td>Soporte</td><td>"soporte 24/7"</td><td>¿En qué país, en qué idioma, con qué tiempo de respuesta contractual?</td></tr>
                </tbody>
              </table>
            </div>

            <p>Si un proveedor no puede responder estas preguntas con números, el problema no son las preguntas.</p>
                """,
            },
        ],
        "taller": {
            "titulo": "Taller: matriz de decisión de un proyecto de robotización",
            "html": """
            <p>El objetivo es construir la herramienta que se reutiliza en toda la ruta de decisión: una matriz de cuatro columnas y cinco filas que obliga a nombrar el problema antes de mirar el catálogo.</p>
            <ol class="steps">
              <li><strong>Liste cinco tareas de mantenimiento</strong> de su propio activo, con la frecuencia anual real, no la teórica del manual.</li>
              <li><strong>Valore cada una</strong> en riesgo para personas, criticidad del servicio y dificultad de ejecución humana.</li>
              <li><strong>Clasifique cada tarea</strong> en inspección o intervención. Es la columna que decide la barrera de seguridad.</li>
              <li><strong>Descarte las de valor bajo</strong> en las tres columnas. El error más común es empezar por la tarea más interesante y no por la que más cuesta.</li>
              <li><strong>Escoja una sola tarea</strong> como piloto y escriba el criterio de éxito en una frase medible.</li>
            </ol>
            <p>Una matriz bien construida suele dejar una o dos filas, no diez. Eso es una buena señal: significa que la restricción se entendió.</p>
            """,
            "entrega": (
                "Una matriz de una página con las cinco tareas, sus tres valores, su clasificación "
                "y una frase de criterio de éxito para el piloto elegido."
            ),
        },
        "resumen_html": """
            <p>El argumento central para la gerencia es simple: el sector eléctrico no Robbie por entusiasmo la automatización de su infraestructura. Lo hizo porque era el único donde el costo de un error —una línea caída, una viuda electrocutada— justificaba pagar por robots que en otra industria serían carísimos.</p>
            <p>Ese argumento tiene una contraparte útil: <strong>si el problema no es de ese calibre, el robot probablemente no lo resuelva.</strong> El valor de un robot de red está en las tareas que nadie quiere hacer dos veces al año, a la intemperie, en altura, sobre un activo que no se puede sacar de servicio. En cualquier otro caso, una cámara fija o un dron de alquiler resuelve más barato.</p>
        """,
    },

    # ------------------------------------------------------------------ 02
    {
        "num": "02",
        "titulo": "Conocimiento de la línea eléctrica",
        "lead": (
            "Torres, conductores, herrajes y aisladores: el activo que hay que "
            "conocer antes de intentar robotizarlo, y las fallas que la inspección "
            "autónoma debe detectar."
        ),
        "resumen": "Torres, conductores, herrajes y aisladores. El activo que hay que conocer para poder robotizarlo.",
        "icono": "network",
        "meta": [
            ("clock", "90 min de lectura"),
            ("doc", "Módulo 2 de 10"),
            ("network", "Base técnica del activo"),
        ],
        "objetivos": [
            "Nombrar las partes de una torre y distinguir elconductor de potencia del conductor de puesta a tierra.",
            "Reconocer los cuatro componentes que concentran la mayoría de los defectos de una línea aérea.",
            "Asociar cada modo de falla con el sensor que lo detecta, para no medir lo que no se va a Romper.",
            "Construir la ficha de activo de un tramo, que es el insumo mínimo de cualquier piloto.",
        ],
        "secciones": [
            {
                "h2": "Anatomía de una línea aérea",
                "html": """
            <p>Una línea de transmisión no es "un cable entre dos torres". Es un conjunto de elementos con nombres normalizados, y cada uno falla de una manera distinta. El robot que se diseña para inspeccionar herrajes no sirve para inspeccionar conductores: cambian la distancia de trabajo, el ángulo y el sensor.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Elemento</th><th>Función</th><th>Falla típica</th><th>Visible a simple vista</th></tr>
                </thead>
                <tbody>
                  <tr><td>Estructura (torre)</td><td>Sostiene y da altura a los conductores.</td><td>Corrosión en la base,_members deformados, pernos flojos, soldaduras fisuradas.</td><td>Sí, de cerca.</td></tr>
                  <tr><td>Conductor</td><td>Transporta la energía.</td><td>Rotura de strand, pérdida de tensión y punto caliente por mal apriete.</td><td>A veces; el resto necesita instrumentación.</td></tr>
                  <tr><td>Herraje</td><td>Conecta conductor con aislador y estructura.</td><td>Corrosión, deformación, fisura, perno que cede.</td><td>Sí, pero a corta distancia.</td></tr>
                  <tr><td>Aislador</td><td>Aíslagallerygallery el conductor de la estructura manteniendo la distancia eléctrica.</td><td>Contaminación, grieta, descarga parcial, pérdida de aislamiento.</td><td>La grieta sí; la descarga parcial no.</td></tr>
                  <tr><td>Puesta a tierra</td><td>Canaliza a tierra las corrientes de falla.</td><td>Corrosión de la malla, resistencia excesiva delelectrodo.</td><td>No: hay que medirla.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout callout-warn">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-shield"/></svg>El detalle que más se olvida</p>
              <p>Los <strong>aisladores de cadena</strong> soportan el conductor y son el punto donde la inspección robótica aporta más: son pequeños, están a la altura exacta de trabajo del robot, y son el componente que más se degrada por contaminación y por descargas parciales. Si un robot de red va a tener un solo destino útil, ese es el primero.</p>
            </div>
                """,
            },
            {
                "h2": "Los conductores y por qué se distinguen entre sí",
                "html": """
            <p>El conductor es el elemento más caro y más crítico de la línea, y el que peor se inspecciona con métodos visualess. Su composición determina tanto el comportamiento térmico como la vida útil.</p>
            <ul class="bullets">
              <li><strong>ACSR</strong> (aluminio-acero): el más usado en transmisión. Alma de aluminio con núcleo de acero para la resistencia mecánica.</li>
              <li><strong>AAAC</strong> (aluminio-acero-aluminio): alternativa más ligera, común en zonas costeras o de baja tensión mecánica.</li>
              <li><strong>ACCC</strong> (conductor de aluminio con núcleo composite): núcleo de fibra de vidrio y carbono. Menos dilatación térmica, más caro, en líneas nuevas de alta exigencia.</li>
              <li><strong>OPGW</strong>: fibra óptica embebida en el alma del conductor. Sirve de sensor distribuido para temperatura y tensión. Es la vía de datos ideal porque no necesita cable ni radio.</li>
              <li><strong>ADSS</strong>: fibra óptica auto-soportada, colgada bajo el conductor, más barata de instalar y con su propia problemática de galopamiento.</li>
            </ul>

            <div class="callout">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-thermal"/></svg>Consecuencia práctica</p>
              <p>Cuando el conductor lleva fibra embebida (OPGW), buena parte de lo que se le pedía al robot de inspección ya se puede medir desde la sala de control. Eso no vuelve innecesario al robot: vuelve al robot <strong>más útil en lo que solo él puede ver</strong> — el herraje, el aislador, la estructura. Un buen proyecto detecta esta superposición antes de gastar presupuesto en medir lo que ya estaba medido.</p>
            </div>
                """,
            },
            {
                "h2": "Los herrajes: donde se concentra la mayoría de los defectos",
                "html": """
            <p>Los herrajes son piezas metálicas pequeñas que conectan conductor, aislador y estructura. Son la fuente número uno de hallazgos en inspección de líneas aéreas, por tres razones que se combinan:</p>
            <ol class="steps">
              <li><strong>Son muchos.</strong> Una torre tiene decenas, y una línea tiene miles.</li>
              <li><strong>Estánuban Working en compresión y en tensión</strong>, con cargas cíclicas de viento y hielo que Lester el metal.</li>
              <li><strong>Son barato de inspeccionar.</strong> El elemento barato que se rompe es el que nadie miró.</li>
            </ol>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Herraje</th><th>Riesgo principal</th><th>Cómo se detecta</th></tr>
                </thead>
                <tbody>
                  <tr><td>Grapa de compresión</td><td>Pérdida de tensión del conductor si resbala.</td><td>Inspección visual a corta distancia + termografía si hay punto caliente.</td></tr>
                  <tr><td>Conector de línea</td><td>Corrosión en la cara interior; falla catastrófica si revienta.</td><td>Visual + medición de resistencia de contacto en mantenimiento.</td></tr>
                  <tr><td>Grapa de suspensión</td><td>Deslizamiento o pérdida de apoyo del conductor.</td><td>Visual; comparar posición respecto al aislador.</td></tr>
                  <tr><td>Abrazadera de puesta a tierra</td><td>Corrosión que corta el camino a tierra.</td><td>Visual + medición de resistencia de la malla.</td></tr>
                </tbody>
              </table>
            </div>

            <p>El hallazgo clásico de inspección robótica en herrajes es el <strong>perno flojo o ausente</strong>. Es un defecto que un operario ve en diez segundos con una binocular desde el suelo, y que sin embargo aparece en el reporte de un robot porque nadie lo revisó a tiempo. Por eso el robot se justifica en el <em>triage</em>, no en el reemplazo del operario.</p>
                """,
            },
            {
                "h2": "Subestaciones: el otro terreno natural",
                "html": """
            <p>Aunque el curso se centra en líneas, el mayor retorno temprano de la robótica de red está en subestaciones, y conviene entender por qué antes de empezar por las torres.</p>
            <ul class="bullets">
              <li>Es un recinto <strong>cerrado y con acceso vehicular</strong>: la logística es mucho más simple que en una torre.</li>
              <li>El equipo es <strong>más denso y más caro</strong>: un transformador o un interruptor resuelve más dinero que un tramo de línea entero.</li>
              <li>Las fallas son <strong>visuales y térmicas</strong>: exactamente lo que los sensores de inspección.Good detectan bien.</li>
              <li>La <strong>altura es moderada</strong>: entre uno y seis metros, sin arnés ni escala.</li>
              <li>El operador puede <strong>acompañar al robot</strong>: es el mejor lugar para un piloto de bajo riesgo.</li>
            </ul>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>Recomendación</p>
              <p>Si va a empezar un programa de robótica de red, empiece por una subestación. El costo de entrada es menor, el tiempo de despliegue es menor y el riesgo reputacional de un error es menor. La altura y la línea aérea llegan después, cuando la organización ya sabe operar robots.</p>
            </div>
                """,
            },
            {
                "h2": "Modos de falla y su firma detectable",
                "html": """
            <p>La clave para diseñar una inspección útil es ir al revés: partir del defecto que se quiere encontrar y deducir qué hay que medir.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Defecto</th><th>Firma física</th><th>Sensor que la detecta</th><th>Detectable desde el suelo</th></tr>
                </thead>
                <tbody>
                  <tr><td>Punto caliente en conexión</td><td>Delta T respecto a vecinos.</td><td>Termografía radiométrica.</td><td>Sí, con elright lente.</td></tr>
                  <tr><td>Pérdida de aislamiento</td><td>Descarga parcial visible u audible.</td><td>Cámara UV, micrófono, detección ultrasónica.</td><td>No de forma confiable.</td></tr>
                  <tr><td>Corrosión de estructura</td><td>Pérdida de sección, descascarillado.</td><td>Cámara RGB de alta resolución + perfil de color.</td><td>Parcialmente.</td></tr>
                  <tr><td>Deformación de member</td><td>Geometría fuera de patrón.</td><td>LiDAR o fotogrametría.</td><td>No.</td></tr>
                  <tr><td>Rotura de strand</td><td>Pérdida de sección visible en el conductor.</td><td>Cámara + telescopio; a veces solo con tensiondata.</td><td>Con difficulty.</td></tr>
                  <tr><td>Degradación de aislador</td><td>Contaminación uniforme, grieta, metal flashing.</td><td>Cámara + UV + inspección dieléctrica.</td><td>Sí, la contaminación.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>El filtro de la última columna</p>
              <p>Esa columna vale más que todo el resto de la tabla. Un defecto que se ve desde el suelo con un teleobjetivo de 400 mm no necesita un robot para <em>detectarse</em>; necesita un robot solo si además se quiere <em>medirlo con precisión y registrar la evidencia</em>. La decisión deonomy robotización debe empezar por esa diferencia, porque determina el presupuesto de todo el proyecto.</p>
            </div>
                """,
            },
        ],
        "taller": {
            "titulo": "Taller: ficha de activo de un tramo",
            "html": """
            <p>Toda especificación de robot arranca con una ficha del activo, no con una lista de requisitos del equipo. El entregable de este taller es esa ficha, y es la que se le va a pedir a cualquier proveedor.</p>
            <ol class="steps">
              <li><strong>Delimite el tramo</strong> con número de torres, longitud en km y nivel de tensión.</li>
              <li><strong>Describa la estructura</strong>: tipo de torre, altura, material, y si tiene escalera o no.</li>
              <li><strong>Liste los tipos de herraje y aislador</strong> con sus cantidades aproximadas por torre.</li>
              <li><strong>Identifique el conductor</strong>: tipo y si lleva OPGW o ADSS.</li>
              <li><strong>Registre los últimos cuatro años de hallazgos</strong> por tipo. Esta es la columna que decide la prioridad.</li>
              <li><strong>Liste los puntos sin acceso</strong>: pendientes, alojamientos, discrepancias de nivel.</li>
            </ol>
            <p>Una ficha bien hecha suele revelar que el 60% de los hallazgos de los últimos años se concentran en menos de tres tipos de componente. Eso es exactamente el dato que justifies el robot.</p>
            """,
            "entrega": (
                "Ficha de activo de una página para un tramo real, con el histórico de hallazgos por tipo de "
                "componente y la lista de puntos sin acceso."
            ),
        },
        "resumen_html": """
            <p>Para la gerencia, la lección de este módulo es que <strong>el robot no se compra, se asigna</strong>. Un robot de red que se despliega sobre un activo cuyos componentes y modos de falla nadie ha analizado está disposant de una cámara móvil cara.</p>
            <p>La inversión en la ficha de activo es la de mejor retorno de todo el proyecto: cuesta semanas, no millones, y es la que evita comprar la plataforma equivocada o medir dos veces lo mismo.</p>
        """,
    },

    # ------------------------------------------------------------------ 03
    {
        "num": "03",
        "titulo": "El robot trepador y las plataformas de movilidad",
        "lead": (
            "Cinemática del trepador, adherencia sobre acero galvanizado y el panorama "
            "completo de plataformas: cuadrúpedos, drones, vehículos terrestres y "
            "submarinos."
        ),
        "resumen": "Mecánica y cinemática del trepador, y el panorama de drones, UGV y UUV.",
        "icono": "drone",
        "meta": [
            ("clock", "90 min de lectura"),
            ("doc", "Módulo 3 de 10"),
            ("robo", "Plataformas y cinemática"),
        ],
        "objetivos": [
            "Explicar el compromiso entre velocidad y adherencia en un robot trepador.",
            "Comparar las cinco familias de plataforma en costo, capacidad de carga útil y capacidad de intervención.",
            "Calcular de forma aproximada la carga útil disponible una vez descontado el peso de la estructura y la batería.",
            "Identificar la plataforma correcta para un tramo dado, justificando la elección con el activo del Módulo 02.",
        ],
        "secciones": [
            {
                "h2": "Anatomía de un robot trepador de torre",
                "html": """
            <p>Un trepador es, en su forma más simple, un mecanismo de sujeción que se desplaza por un elemento estructural vertical —un angular, un tubo o un alma de perfil— y que transporta una carga útil. Todo lo demás es consecuencia de cómo resuelve dos problemas.</p>

            <h3>El primer problema: cómo se sujeta</h3>
            <p>Existen tres familias, y la elección define el activo sobre el que el robot puede trabajar:</p>
            <ul class="bullets">
              <li><strong>Ventosa o agarre suave:</strong> se adhiere por presión negativa o por contacto elástico. Es el método más rápido y el más inofensivo para la estructura, y exige superficie lisa y limpia.</li>
              <li><strong>Pinza o mordaza positiva:</strong> abraza el elemento y se ancla mecánicamente. Aguanta más y no depende de la superficie, pero deja marca y hay que verificar el par de apriete.</li>
              <li><strong>Ganchos o rodillos:</strong> envolvente por un lado en estructuras de celosía. Es la opción para torres de celosía de acero, donde no hay un elemento continuo por el que trepar.</li>
            </ul>

            <h3>El segundo problema: dónde está la línea</h3>
            <p>En una torre de celosía el robot sube por un alma, pero el conductor está a varios metros de distancia horizontal y por encima. Ahí es donde entra la cinemática de la plataforma articulada y el brazo de inspección, y por eso casi ningún trepador sube "y ya está": sube, se posiciona y <em>alcanza</em>.</p>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>La cifra que decide proyectos</p>
              <p>En cualquier plataforma trepadora, el número que hay que pedir y verificar es el <strong>alcance de inspección con carga útil instalada</strong>: cuán lejos del eje de la torre llega el sensor, y cuánto pesa lo que lleva. Un robot con excelente adherencia y brazo corto es útil en estructura, pero no ve aisladores.</p>
            </div>
                """,
            },
            {
                "h2": "El compromisofundamental: velocidad contra adherencia",
                "html": """
            <p>En un trepador hay un compromiso físico que no se puede negociar. Cuanto más rápido se mueve, más fuerza se necesita en los actuadores y más peso deben soportar los acoplamientos; y cuanto más seguros y discretos son los actuadores, más lento se mueve.</p>
            <p>Esto se traduce en tres números que hay que comparar entre proveedores y que rara vez aparecen juntos en una ficha técnica:</p>
            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Parámetro</th><th>Qué mide</th><th>Por qué importa</th></tr>
                </thead>
                <tbody>
                  <tr><td>Velocidad de ascenso</td><td>Metros por hora en el perfil declarado.</td><td>Define cuántos minutos se tarda en una torre y, con eso, cuántos operarios y cuántas horas de ventana.</td></tr>
                  <tr><td>Fuerza de sujeción</td><td>Newtons de retención, y factor de seguridad sobre peso total.</td><td>Determina si el robot sobrevive a ráfaga de viento con la carga desplazada.</td></tr>
                  <tr><td>Par máximo</td><td>Par de torsión en el acoplamiento principal.</td><td>Es el límite frente a torsión por viento, la causa clásica de caída en torres de celosía.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout callout-warn">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-shield"/></svg>Advertencia</p>
              <p>La velocidad máxima publicada casi siempre es la velocidad <em>en vacío</em>, sin carga útil y sin viento. Pregunte siempre por la velocidad con carga nominal y en el perfil de viento de su tramo. Un número de especificación en esta industria rara vez es el número de campo.</p>
            </div>
                """,
            },
            {
                "h2": "El panorama de plataformas",
                "html": """
            <p>Cinco familias cubren hoy la práctica totalidad de los casos de uso de interés:</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Familia</th><th>FORTALEZAS</th><th>Debilidades</th><th>Mejor terreno</th></tr>
                </thead>
                <tbody>
                  <tr><td>Cuadrúpedo (UGV de patas)</td><td>Se adapta a terreno irregular; redundancia natural; trepa escalones y rejillas.</td><td>Consumo alto; lento; caro.</td><td>Subestaciones, patios, chantier.</td></tr>
                  <tr><td>Trepador de torre</td><td>Llega a la altura exacta del aislador y del herraje; carga útil estable.</td><td>Solo en estructura compatible; requiere acceso a la base.</td><td>Torres de transmisión y distribución.</td></tr>
                  <tr><td>Drone (multirrotor)</td><td>Rápido de desplegar; cubre kilómetros de línea por día; no necesita base fija.</td><td>Depende del clima y del viento; poca carga útil; autonomía limitada por batería.</td><td>Líneas largas, corredor abierto.</td></tr>
                  <tr><td>Drone (ala fija / VTOL)</td><td>Autonomía de horas y gran alcance de corredor.</td><td>No puede_STOP en el punto ni tomar un contacto; útil para mapeo y detección de corredor.</td><td>Inspección de corredor extenso, detección de intrusión en servidumbre.</td></tr>
                  <tr><td>Submarino (UUV)</td><td>El único que inspecciona cables submarinos sin cortar servicio.</td><td>Tecnología y costo muy altos; navegación relativa.</td><td>Cables submarinos de interconexión.</td></tr>
                </tbody>
              </table>
            </div>

            <div class="callout">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>Dónde está la frontera real</p>
              <p>Hay una frontera clara entre <strong>ver</strong> y <strong>tocar</strong>. El dron llega al conductor y lo examina; difícilmente lo toca. La plataforma trepadora llega al herraje y puede agarrarlo. Mientras el proyecto sea de inspección, el dron gana en costo por punto inspeccionado; en cuanto aparezca un requisito de manipulación, la plataforma con brazo gana, aunque sea más lenta y más cara.</p>
            </div>
                """,
            },
            {
                "h2": "Carga útil: la cuenta que casi nadie hace",
                "html": """
            <p>La ficha técnica dice "carga útil máxima". La pregunta correcta es qué queda después de pagar el resto del robot.</p>
            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-sensor"/></svg>Fórmula de trabajo</p>
              <p>Carga útil disponible = carga útil nominal − peso del sensor − peso del brazo de inspección − peso del cableado y de las protecciones − peso de la batería de reserva.</p>
              <p>En plataformas pequeñas este cálculo suele dejar un margen muy pequeño. Si el proyecto necesita un manipulator abrasivo y una cámara de alto rango dinámico a la vez, la plataforma escolhida probablemente no admita ambos.</p>
            </div>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Elemento de la carga útil</th><th>Peso aproximado</th><th>¿Se puede omitir?</th></tr>
                </thead>
                <tbody>
                  <tr><td>Cámara RGB de inspección con zoom</td><td>0,8 – 2 kg</td><td>Nunca: es la razón de ser del viaje.</td></tr>
                  <tr><td>Cámara termográfica radiométrica</td><td>0,3 – 1 kg</td><td>Solo si el defecto buscado es visible.</td></tr>
                  <tr><td>Brazo articulado de 4 grados de libertad</td><td>4 – 12 kg</td><td>No, si se quiere alcanzar herraje desde el alma.</td></tr>
                  <tr><td>Herramienta de torque</td><td>3 – 8 kg</td><td>Solo en proyectos de intervención.</td></tr>
                  <tr><td>Reflector e iluminación</td><td>1 – 3 kg</td><td>De noche, nunca.</td></tr>
                  <tr><td>Batería de reserva para operación en frío</td><td>5 – 20 kg</td><td>Depende del clima del tramo.</td></tr>
                </tbody>
              </table>
            </div>

            <p>Los valores de la tabla son órdenes de magnitud de mercado, no especificaciones de un fabricante concreto. Sirven para hacer la cuenta de arriba en la etapa de pre-facturación y decidir si hace falta pedir una plataforma de la siguiente categoría.</p>
                """,
            },
            {
                "h2": "Variables de entorno que deciden el proyecto",
                "html": """
            <p>Antes de comparar plataformas hay que leer el clima del tramo, porque es lo que invalida más especificaciones.</p>
            <ul class="bullets">
              <li><strong>Racha de viento máxima.</strong> En muchas zonas del interior de Colombia y del Perú, más de la mitad del año hay ráfagas por encima de lo que cualquier drone soporta con carga útil. Un proyecto de dron mal planificado se cancela solo, sin código de error.</li>
              <li><strong>Altitud.</strong> Por encima de 3 000 m la densidad del aire cae y la capacidad de sustentación y la autonomía bajan. El número del fabricante es a nivel del mar.</li>
              <li><strong>Temperatura mínima.</strong> El frío reduce capacidad de batería de litio y vuelve frágil a los sellos y a las juntas.</li>
              <li><strong>Lluvia y humedad.</strong> Restringe la cámara y la termografía; exige un grado de protección real, no nominal.</li>
              <li><strong>Espacio aéreo.</strong> Con ionizing, con líneas de alta tensión o en corredor de aeropuerto, la operación de dron se vuelve un trámite, y a veces un trámite imposible.</li>
            </ul>
                """,
            },
        ],
        "taller": {
            "titulo": "Taller: selección de plataforma por tramo",
            "html": """
            <p>Se toma la ficha de activo del Módulo 02 y se aplica el método. El entregable es una recomendación argumentada de una línea, no un equipo concreto.</p>
            <ol class="steps">
              <li><strong>Delimite la tarea.</strong> Una sola tarea, un solo componente objetivo: por ejemplo "detectar descargas parciales en aisladores de cadena".</li>
              <li><strong>Fije la altura de trabajo</strong> necesaria y la distancia horizontal al objetivo desde el elemento estructural.</li>
              <li><strong>Descarte plataformas</strong> que no alcancen esa geometría, anotando el motivo.</li>
              <li><strong>Sobreviva</strong> las dos que queden con el clima del módulo 01 y 02: viento, altitud, temperatura.</li>
              <li><strong>Haga la cuenta de carga útil</strong> con los sensores del módulo 04. Si no cierra, suba de categoría o recorte alcance.</li>
              <li><strong>Escriba la justificación en un párrafo</strong> que un committee pueda leer sin asking clarifying questions.</li>
            </ol>
            <p>Si el párrafo termina siendo largo o llena de "y también puede…", probablemente la tarea elegida fue demasiado ambiciosa para un solo piloto.</p>
            """,
            "entrega": (
                "Nota de selección de plataforma de una página: tarea, geometría, candidatos descartados y su "
                "motivo, candidatos sobrevivientes y justificación final."
            ),
        },
        "resumen_html": """
            <p>La idea que debe quedar para la gerencia: <strong>el dron y el trepador no compiten, se complementan</strong>. El dron da cobertura y velocidad sobre kilómetros de corredor; el trepador da precisión y capacidad de intervención sobre un punto. Un programa maduro usa los dos, y usa el dron para decidir a dónde va el trepador.</p>
            <p>Esa lógica es además la que ordena el presupuesto: primero se paga por <em>saber</em> dónde está el problema, después por <em>arreglar</em> el problema. Es un orden de inversión que casi nunca es el que propone el proveedor, y siempre es el que protege el presupuesto.</p>
        """,
    },

    # ------------------------------------------------------------------ 04
    {
        "num": "04",
        "titulo": "Sensores para inspección",
        "lead": (
            "Termografía, visión, acústica y LiDAR: qué detecta cada sensor, con qué "
            "límites, y cómo capturar bien la evidencia."
        ),
        "resumen": "Termografía, visión, acústica y LiDAR. Qué detecta cada uno y cómo se captura bien.",
        "icono": "thermal",
        "meta": [
            ("clock", "90 min de lectura"),
            ("doc", "Módulo 4 de 10"),
            ("thermal", "Termografía, visión, LiDAR"),
        ],
        "objetivos": [
            "Emparejar cada modo de falla del Módulo 02 con el sensor que realmente lo detecta.",
            "Explicar por qué la termografía malTomada produce hallazgos falsos.",
            "Distinguir las medidas que exigen una geometría conocida de las que se pueden hacer en movimiento.",
            "Diseñar un plan de captura para un tramo, con distancia, ángulo y referencias.",
        ],
        "secciones": [
            {
                "h2": "Termografía: la más útil y la más traicionera",
                "html": """
            <p>La cámara termográfica es el sensor con mejor relación entre valor y costo en toda la inspección de redes: detecta elcalor, y el calor es la huella de casi todos los defectos resistivos. El problema es que mide mal con facilidad.</p>

            <h3>El principio</h3>
            <p>La cámara mide radiación infrarroja y calcula una temperatura de superficie. La temperatura que se calcula es correcta solo si la cámara sabe <em>cuánto</em> de lo que ve es emisión propia de la superficie, y eso se controla con la emisividad. Un herraje galvanizado nuevo tiene emisividad baja; uno con corrosión y óxido la tiene alta. Si no se corrige, la misma lectura da dos temperaturas distintas según el operario que la tomó.</p>

            <h3>Los tres errores que generan hallazgos falsos</h3>
            <ol class="steps">
              <li><strong>Emisividad no ajustada.</strong> Causa número uno. Galvanizado, aluminio y óxido dar lecturas incompatibles entre sí en la misma imagen.</li>
              <li><strong>Reflexión de fondo.</strong> El metal pulido refleja el sol, el operador o las torres vecinas: la imagen brilla donde no hay defecto.</li>
              <li><strong>Distancia y ángulo incorrectos.</strong> La cámara enfoca a un rango fijo; a distancia y con ángulo oblicuo, el píxel medido no es el punto que el operario cree.</li>
            </ol>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-target"/></svg>La regla operativa</p>
              <p>La termografía no se lee en pantalla durante la inspección. Se <strong>extrae</strong>: se aísla cada punto de conexión del resto de la escena y se compara con puntos equivalentes. Un termograma sin punto de referencia conocido no es evidencia.</p>
            </div>
                """,
            },
            {
                "h2": "Visión: el sensor que más información produce y peor se aprovecha",
                "html": """
            <p>La cámara produce la mayor cantidad de datos por segundo y es la que más veces se desperdicia, porque se guarda mucho y se analiza poco.</p>
            <ul class="bullets">
              <li><strong>RGB de alta resolución.</strong> El caballo de batalla: grietas, corrosión, deformaciones, condición general. Necesita luz y distancia corta para resolver una fisura.</li>
              <li><strong>Visión multiespectral.</strong> Distingueixels materiales por firma espectral. Es lo que permite separar óxido, Alonso y lichen sobre el mismo aislador.</li>
              <li><strong>Cámara UV.</strong> Hace visibles las descargas parciales de corona como puntos luminosos. Es de las pocas técnicas que detecta en vivo un defecto que aún no ha causado falla.</li>
              <li><strong>Cámara infrarroja de onda larga.</strong> Complementa a la RGB en niebla, humo o penumbra: ve lo que la visible no ve.</li>
            </ul>

            <div class="callout">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-doc"/></svg>Evidencia</p>
              <p>Para que una imagen sea prueba, necesita tres cosas que un robot puede y un operario con celular no: <strong>marcador de escala en la escena</strong>, <strong>georreferencia y orientación</strong>, y <strong>identificación del componente</strong> al que corresponde. Sin las tres, la foto sirve para estética y no para el expediente técnico.</p>
            </div>
                """,
            },
            {
                "h2": "LiDAR y navegación: medir la geometría del activo",
                "html": """
            <p>El LiDAR emite pulsos y mide el tiempo de retorno para construir una nube de puntos. En inspección de red aporta dos cosas distintas que a menudo se confunden.</p>

            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Uso</th><th>Qué entrega</th><th>Costo</th><th>Cuando se justifica</th></tr>
                </thead>
                <tbody>
                  <tr><td>Navegación y localization</td><td>Posición precisa del robot para georreferenciar la inspección.</td><td>Bajo si el robot ya lo trae.</td><td>Siempre, si se van a registrar hallazgos.</td></tr>
                  <tr><td>Inspección geométrica</td><td>Deformación de una torre, flecha del conductor, distancia aMagnets de seguridad.</td><td>Alto.</td><td>Cuando hay una deformación sospechada que hay que medir.</td></tr>
                  <tr><td>Mapeo de corredor</td><td>Nube de puntos del servidumbre para detectarvegetación invasora.</td><td>Alto, y mucho dato.</td><td>En corredores de gran extensión, con dron de ala fija.</td></tr>
                </tbody>
              </table>
            </div>

            <p>Regla práctica: el LiDAR de navegación se paga solo. El LiDAR de inspección es una inversión de proyecto y hay que justificarla con un defecto concreto que se quiere medir.</p>
                """,
            },
            {
                "h2": "Sensores acústicos: escuchar la descarga parcial",
                "html": """
            <p>La descarga parcial genera un pulso acústico y una emisión ultrasónica. Un micrófono convencional la detecta cuando es audible —el coronamiento audible de un aislador sucio— y un transductor de presión ultrasónica la detecta siempre, incluso con lluvia, porque el aire atenúa menos el ultrasonido que el sonido.</p>
            <ul class="bullets">
              <li><strong>Limitación principal:</strong> el sonido se propaga mal en el viento y se atenúa con la lluvia. Un registro acústico tiene que ir acompañado del estado del tiempo en ese momento.</li>
              <li><strong>Limitación de alcance:</strong> la fuente se localiza mal si hay más de un punto activo en la misma estructura.</li>
              <li><strong>Ventaja:</strong> es de los pocos sensores que detectan un defecto <em>antes</em> de que exista un daño visible, lo que lo convierte en la herramienta clave de mantenimiento predictivo.</li>
            </ul>
                """,
            },
            {
                "h2": "Sensores que casi se olvidan en el presupuesto",
                "html": """
            <p>Entre el 80% y el 90% del presupuesto de sensores suele ir en cámaras. Los quegenesis la diferencia entre una inspección y una prueba son más baratos:</p>
            <div class="table-wrap">
              <table>
                <thead>
                  <tr><th>Sensor</th><th>Costo relativo</th><th>Qué habilita</th></tr>
                </thead>
                <tbody>
                  <tr><td>IMU de precisión</td><td>Muy bajo</td><td>Saber exactamente hacia dónde miraba la cámara en cada disparo. Sin esto no hay georreferencia posible.</td></tr>
                  <tr><td>RTK GNSS</td><td>Medio</td><td>Posición centimétrica en exterior, sin estación total.</td></tr>
                  <tr><td>Iluminación propia</td><td>Bajo</td><td>Convierte una inspección de día en una de turno noche. Multiplica los puntos por torre.</td></tr>
                  <tr><td>Cámara de contexto</td><td>Bajo</td><td>Una vista amplia de la torre por cada punto de detalle. Sin ella, el inspector tiene que adivinar dónde está.</td></tr>
                  <tr><td>Sensor de distancia de seguridad</td><td>Medio</td><td>La medición que demuestra que el robot mantuvo la distancia mínima. Es evidencia, no safety extra.</td></tr>
                  <tr><td>Sincronizador de tiempo</td><td>Muy bajo</td><td>Correlacionar imagen, temperatura y posición en un mismo instante.</td></tr>
                </tbody>
              </table>
            </div>
            <div class="callout callout-warn">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-shield"/></svg>Criterio de inversión</p>
              <p>Presupueste un <strong>35% del costo total en sensores</strong> y un <strong>10% en iluminación y contexto</strong>. Ese segundo número es el que casi todos recortan primero y el que más rápido se nota en el informe de hallazgos.</p>
            </div>
                """,
            },
        ],
        "taller": {
            "titulo": "Taller: plan de captura de un tramo",
            "html": """
            <p>Se cierra el círculo con los tres módulos anteriores: ficha de activo, plataforma y ahora sensores. El entregable es la especificación de la captura.</p>
            <ol class="steps">
              <li><strong>Liste los tres defectos prioritarios</strong> según el histórico del módulo 02, no según el catálogo del proveedor.</li>
              <li><strong>Asigne un sensor a cada uno</strong> y descarte los que no aportan a esos tres.</li>
              <li><strong>Fije la geometría de captura:</strong> distancia, ángulo y número de tomas por componente. Nada de "cuantas fotos haya".</li>
              <li><strong>Defina la evidencia:</strong> marcador de escala, georreferencia, identificador de componente y condición del ambiente.</li>
              <li><strong>Escriba el criterio de calidad de la toma</strong> —qué hace que una imagen sea rechazada en campo— y css.coloque el umbral de reintento.</li>
              <li><strong>Calcule el volumen</strong> de la jornada y compruebe que cabe en el ancho de banda de transmisión.</li>
            </ol>
            <p>El paso 6 es donde aparecen las sorpresas. Una hora de vídeo de una torre puede pesar más que todo el equipo, y ese dato hay que llevarlo a la discussion de infraestructura antes de la primera salida.</p>
            """,
            "entrega": (
                "Plan de captura de dos páginas: defectos prioritarios, sensor asignado, geometría, requisitos de "
                "evidencia y volumen de datos por jornada."
            ),
        },
        "resumen_html": """
            <p>El mensaje para la gerencia es que <strong>el sensor no genera información, la calidad de la captura la genera</strong>. Con la misma cámara, dos equipos pueden entregar el doble de defectos reales o el doble de falsos positivos, y la diferencia no está en el modelo de IA sino en la disciplina de captura: distancia, ángulo, iluminación, escala y referencia.</p>
            <p>Por eso la inversión en especificación de captura rinde más que la inversión en un sensor más caro. Es también el argumento que justifica exigir evidencia estructurada a un proveedor: no es burocracia, es lo que hace que los hallazgos valgan.</p>
        """,
    },
]