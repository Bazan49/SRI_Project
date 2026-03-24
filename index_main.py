import sys
import asyncio
from pathlib import Path
from datetime import datetime

# Asegura que el paquete `src/` esté en el path cuando se ejecuta desde la raíz
ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from DI.continer import SearchContainer
from DataAcquisitionModule.Scraper.scrapedDocument import ScrapedDocument

container = SearchContainer()
container.wire(modules=[__name__])

async def main():
    index_service = container.index_service()
    
    # Tus documentos scraped
    scraped_docs = [
    ScrapedDocument(
        source="bbc",
        url="https://example.com/noticia-1",
        url_normalized="https://example.com/noticia-1",
        title="La economía global muestra signos de recuperación",
        content="La economía mundial está mostrando señales de recuperación tras la crisis reciente. Expertos destacan el crecimiento en varios sectores clave.",
        authors=["Juan Pérez"],
        date=datetime(2024, 3, 10),
        indexed=False,
        embeddings_generated=False
    ),
    # Economía
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/economia/2024/01", 
        url_normalized="https://cubadebate.cu/economia/2024/01",
        title="La economía cubana muestra signos de recuperación",
        content="La economía cubana está mostrando signos de recuperación tras un período difícil. Los sectores turístico y agrícola han liderado el crecimiento. El gobierno ha implementado nuevas políticas para estimular la inversión extranjera.",
        authors=["María García"], date=datetime(2024, 1, 15), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/economia/2024/02",
        url_normalized="https://cubadebate.cu/economia/2024/02",
        title="Sector turístico cubano supera expectativas",
        content="El sector turístico de Cuba ha superado las expectativas de crecimiento este año. Los hoteles报告显示 una ocupación promedio del 85%. Los expertos prevén que el turismo seguirá siendo el motor de la economía nacional.",
        authors=["Carlos López"], date=datetime(2024, 1, 20), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/economia/2024/03",
        url_normalized="https://cubadebate.cu/economia/2024/03",
        title="Inversiones extranjeras en Cuba aumentan",
        content="Las inversiones extranjeras en Cuba han aumentado significativamente en los últimos meses. Empresas de España, México y Canadá han mostrado interés en el mercado cubano. Los sectores más atractivos son el turismo y la energía renovable.",
        authors=["Ana Martínez"], date=datetime(2024, 2, 5), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/economia/2024/04",
        url_normalized="https://cubadebate.cu/economia/2024/04",
        title="Producción agrícola supera metas establecidas",
        content="La producción agrícola en Cuba ha superado las metas establecidas para este año. Los cultivos de arroz y frijoles han tenido un buen rendimiento. El gobierno ha invertido en tecnología agrícola para mejorar la eficiencia.",
        authors=["Pedro Sánchez"], date=datetime(2024, 2, 10), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/economia/2024/05",
        url_normalized="https://cubadebate.cu/economia/2024/05",
        title="Crisis económica mundial afecta mercados",
        content="La crisis económica mundial está afectando los mercados internacionales. Los precios del petróleo han bajado y las monedas latinoamericanas se han depreciado. Los analistas warn about la situación económica global.",
        authors=["Laura Rodríguez"], date=datetime(2024, 2, 15), indexed=False, embeddings_generated=False
    ),
    
    # Política
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/politica/2024/01",
        url_normalized="https://cubadebate.cu/politica/2024/01",
        title="Gobierno anuncia nuevas políticas públicas",
        content="El gobierno ha anunciado nuevas políticas públicas para mejorar la educación y la salud. Se invertirá en escuelas y hospitales en todo el país. Las autoridades aseguran que estas medidas beneficiarán a la población.",
        authors=["Juan Pérez"], date=datetime(2024, 1, 18), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/politica/2024/02",
        url_normalized="https://cubadebate.cu/politica/2024/02",
        title="Elecciones municipales serán en 2024",
        content="Las elecciones municipales se celebrarán en el mes de octubre de 2024. Los ciudadanos podrán elegir a sus representantes locales. El proceso electoral será supervisado por organismos internacionales.",
        authors=["Carmen Torres"], date=datetime(2024, 2, 1), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/politica/2024/03",
        url_normalized="https://cubadebate.cu/politica/2024/03",
        title="Relaciones diplomáticas con países vecinos",
        content="Cuba fortalece sus relaciones diplomáticas con países vecinos del Caribe. Se han firmado acuerdos de cooperación en áreas como comercio, cultura y educación. Los embajadores han destacado la importancia del diálogo.",
        authors=["Roberto Díaz"], date=datetime(2024, 2, 8), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/politica/2024/04",
        url_normalized="https://cubadebate.cu/politica/2024/04",
        title="Reforma del sistema judicial avanza",
        content="La reforma del sistema judicial continúa avanzando en el país. Se han implementado nuevos mecanismos para garantizar la transparencia y el acceso a la justicia. Los abogados han participado en la elaboración de las nuevas leyes.",
        authors=["Sofia Hernández"], date=datetime(2024, 2, 20), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/politica/2024/05",
        url_normalized="https://cubadebate.cu/politica/2024/05",
        title="Partido político celebra congreso nacional",
        content="El partido político ha celebrado su congreso nacional con la participación de delegados de todo el país. Se han definido las líneas estratégicas para los próximos años. Los líderes han destacado la unidad del pueblo.",
        authors=["Miguel Fernández"], date=datetime(2024, 3, 1), indexed=False, embeddings_generated=False
    ),
    
    # Salud
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/salud/2024/01",
        url_normalized="https://cubadebate.cu/salud/2024/01",
        title="Nuevo hospital inaugurated en La Habana",
        content="Un nuevo hospital ha sido inaugurado en La Habana con modernas instalaciones. El centro médico cuenta con tecnología de punta y personal especializado. Los pacientes podrán acceder a servicios de alta calidad.",
        authors=["Elena Vargas"], date=datetime(2024, 1, 22), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/salud/2024/02",
        url_normalized="https://cubadebate.cu/salud/2024/02",
        title="Programa de vacunación cubre a toda la población",
        content="El programa de vacunación ha cubierto a toda la población del país. Las autoridades sanitarias reportan altas tasas de inmunización. Las enfermedades prevenibles han disminuido significativamente.",
        authors=["Jorge Morales"], date=datetime(2024, 2, 3), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/salud/2024/03",
        url_normalized="https://cubadebate.cu/salud/2024/03",
        title="Médicos cubanos colaboran en el exterior",
        content="Médicos cubanos continúan colaborando en programas de salud en el exterior. Brigadas médicas han sido enviadas a países de África y América Latina. Los profesionales de la salud han recibido reconocimientos internacionales.",
        authors=["Patricia Reyes"], date=datetime(2024, 2, 12), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/salud/2024/04",
        url_normalized="https://cubadebate.cu/salud/2024/04",
        title="Investigación sobre nuevas medicinas avanza",
        content="Investigadores cubanos avanzan en el desarrollo de nuevas medicinas. Los laboratorios han desarrollado tratamientos innovadores para diversas enfermedades. Los resultados de los estudios clínicos son prometedores.",
        authors=["Andrés Castro"], date=datetime(2024, 2, 18), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/salud/2024/05",
        url_normalized="https://cubadebate.cu/salud/2024/05",
        title="Sistema de salud fortalece atención primaria",
        content="El sistema de salud fortalece la atención primaria en todo el territorio nacional. Se han construido nuevos consultorios del médico de la familia. Los servicios de emergencia han mejorado significativamente.",
        authors=["Lucía Méndez"], date=datetime(2024, 2, 25), indexed=False, embeddings_generated=False
    ),
    
    # Deportes
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/deportes/2024/06",
        url_normalized="https://cubadebate.cu/deportes/2024/06",
        title="El deporte en cuba crece",
        content="El equipo nacional de baseball ha clasificado para el campeonato mundial. Los jugadores han demostrado un excelente desempeño en las clasificatorias. Los herramientfanáticos esperan con ansias la competencia internacional.",
        authors=["Raúl Ortega"], date=datetime(2024, 1, 25), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/deportes/2024/01",
        url_normalized="https://cubadebate.cu/deportes/2024/01",
        title="Equipo de baseball clasifica para el mundial",
        content="El equipo nacional de baseball ha clasificado para el campeonato mundial. Los jugadores han demostrado un excelente desempeño en las clasificatorias. Los herramientfanáticos esperan con ansias la competencia internacional.",
        authors=["Raúl Ortega"], date=datetime(2024, 1, 25), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/deportes/2024/02",
        url_normalized="https://cubadebate.cu/deportes/2024/02",
        title="Atletas cubanos ganan medallas en competencias",
        content="Atletas cubanos han ganado múltiples medallas en competencias internacionales de atletismo. Los deportistas han demostrado un alto nivel de preparación. Los entrenadores destacan el trabajo de las academias deportivas.",
        authors=["Diana Flores"], date=datetime(2024, 2, 6), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/deportes/2024/03",
        url_normalized="https://cubadebate.cu/deportes/2024/03",
        title="Boxeo cubano mantiene hegemonía regional",
        content="El boxeo cubano mantiene su hegemonía en los pugilados regionales. Los	boxeadores han conquistado oro en diversos torneos. Los expertos consideran que Cuba sigue siendo una potencia mundial del boxeo amateur.",
        authors=["Gustavo Peña"], date=datetime(2024, 2, 14), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/deportes/2024/04",
        url_normalized="https://cubadebate.cu/deportes/2024/04",
        title="Fútbol cubano mejora en ranking internacional",
        content="El fútbol cubano ha mejorado su posición en el ranking internacional de selecciones. El equipo nacional ha logrado victorias importantes en las últimas competencias. Los entrenadores trabajan en la formación de nuevos talentos.",
        authors=["Hugo Jiménez"], date=datetime(2024, 2, 22), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/deportes/2024/05",
        url_normalized="https://cubadebate.cu/deportes/2024/05",
        title="Juegos Centroamericanos serán en 2024",
        content="Los Juegos Centroamericanos y del Caribe se celebrarán en 2024. Los atletas cubanos se preparan intensamente para la competencia. Las autoridades deportivas han invertido en modernas instalaciones deportivas.",
        authors=["Marta Delgado"], date=datetime(2024, 3, 5), indexed=False, embeddings_generated=False
    ),
    
    # Cultura
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/cultura/2024/01",
        url_normalized="https://cubadebate.cu/cultura/2024/01",
        title="Festival de cine cubano atrae a visitantes",
        content="El festival de cine cubano ha atraído a miles de visitantes nacionales e internacionales. Se han proyectado películas de reconocidas directoras y directores. El evento promueve la cultura cinematográfica nacional.",
        authors=["Claudia Ruiz"], date=datetime(2024, 1, 28), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/cultura/2024/02",
        url_normalized="https://cubadebate.cu/cultura/2024/02",
        title="Artesanos cubanos exponen sus obras",
        content="Artesanos cubanos exponen sus obras en la feria internacional de artesanía. Los visitantes pueden adquirir piezas únicas de cerámica, tejidos y esculturas. La artesanía cubana es reconocida mundialmente por su calidad.",
        authors=["Fernando Soto"], date=datetime(2024, 2, 7), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/cultura/2024/03",
        url_normalized="https://cubadebate.cu/cultura/2024/03",
        title="Música tradicional cubana se mantiene viva",
        content="La música tradicional cubana se mantiene viva a través de grupos y escuelas de música. Los estudiantes aprenden los géneros auténticos como el son, la rumba y el mambo. Los artistas contemporáneos fusionan lo tradicional con lo moderno.",
        authors=["Rosa Vázquez"], date=datetime(2024, 2, 16), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/cultura/2024/04",
        url_normalized="https://cubadebate.cu/cultura/2024/04",
        title="Escritores cubanos publican nuevas novelas",
        content="Escritores cubanos han publicado nuevas novelas que están recibiendo elogios de la crítica literaria. Las obras abordan temas de la sociedad contemporánea. Las editoriales nacionales e internacionales han mostrado interés.",
        authors=["Alberto Romero"], date=datetime(2024, 2, 24), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/cultura/2024/05",
        url_normalized="https://cubadebate.cu/cultura/2024/05",
        title="Arquitectura histórica se preserva en La Habana",
        content="La arquitectura histórica de La Habana Vieja se preserva gracias a los esfuerzos de restauración. Edificios coloniales han sido recuperados para uso cultural y turístico. Los arquitectos trabajan en la conservación del patrimonio.",
        authors=["Gloria Ibarra"], date=datetime(2024, 3, 3), indexed=False, embeddings_generated=False
    ),
    
    # Tecnología
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/tecnologia/2024/01",
        url_normalized="https://cubadebate.cu/tecnologia/2024/01",
        title="Universidad cubana desarrolla software innovador",
        content="La universidad cubana ha desarrollado un software innovador para la gestión empresarial. El programa permite automatizar procesos y mejorar la eficiencia de las empresas. Los creadores han recibido reconocimientos nacionales.",
        authors=["Ricardo Peña"], date=datetime(2024, 1, 30), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/tecnologia/2024/02",
        url_normalized="https://cubadebate.cu/tecnologia/2024/02",
        title="Internet móvil se expande en el país",
        content="El internet móvil se está expandiendo en todo el territorio nacional. Más comunidades rurales tienen acceso a la red. Las autoridades trabajan para mejorar la conectividad y reducir los costos.",
        authors=["Sandra Mendoza"], date=datetime(2024, 2, 9), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/tecnologia/2024/03",
        url_normalized="https://cubadebate.cu/tecnologia/2024/03",
        title="Científicos crean aplicación para la agricultura",
        content="Científicos cubanos han creado una aplicación móvil para optimizar la agricultura. Los farmers pueden monitorear sus cultivos y recibir recomendaciones técnicas. La herramienta ha sido descargada por miles de usuarios.",
        authors=["Óscar Ramírez"], date=datetime(2024, 2, 17), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/tecnologia/2024/04",
        url_normalized="https://cubadebate.cu/tecnologia/2024/04",
        title="Red de universidades implementa e-learning",
        content="La red de universidades ha implementado plataformas de e-learning para la educación a distancia. Los estudiantes pueden acceder a cursos en línea desde cualquier lugar. La infraestructura tecnológica ha sido modernizada.",
        authors=["Verónica Luna"], date=datetime(2024, 2, 26), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/tecnologia/2024/05",
        url_normalized="https://cubadebate.cu/tecnologia/2024/05",
        title="Inteligencia artificial aplicada a la medicina",
        content="La inteligencia artificial se está aplicando en el campo de la medicina en Cuba. Los sistemas pueden diagnosticar enfermedades con alta precisión. Los investigadores trabajan en nuevos algoritmos para mejorar la atención médica.",
        authors=["Daniel Herrera"], date=datetime(2024, 3, 7), indexed=False, embeddings_generated=False
    ),
    
    # Medio Ambiente
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/medioambiente/2024/01",
        url_normalized="https://cubadebate.cu/medioambiente/2024/01",
        title="Reforestación en toda la isla",
        content="Un programa de reforestación se lleva a cabo en toda la isla. Se han plantado millones de árboles para recuperar áreas boscosas. Los voluntarios participan activamente en las jornadas de siembra.",
        authors=["Eugenio Guzmán"], date=datetime(2024, 2, 2), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/medioambiente/2024/02",
        url_normalized="https://cubadebate.cu/medioambiente/2024/02",
        title="Energías renovables en aumento",
        content="El uso de energías renovables está en aumento en el país. Se han instalado parques solares y eólicos en varias regiones. La transición energética contribuye a la reducción de emisiones de carbono.",
        authors=["Beatriz Pardo"], date=datetime(2024, 2, 11), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/medioambiente/2024/03",
        url_normalized="https://cubadebate.cu/medioambiente/2024/03",
        title="Protección de especies marinas en peligro",
        content="Se implementan medidas para la protección de especies marinas en peligro de extinción. Los santuario marinos han sido ampliados. Las autoridades trabajan con organizaciones internacionales para preservar la biodiversidad.",
        authors=["Francisco Leiva"], date=datetime(2024, 2, 19), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/medioambiente/2024/04",
        url_normalized="https://cubadebate.cu/medioambiente/2024/04",
        title="Cambio climático afecta la agricultura",
        content="El cambio climático está afectando la agricultura en diversas regiones del país. Los fenómenos meteorológicos extremos han causado pérdidas en las cosechas. Los científicos estudian estrategias de adaptación.",
        authors=["Isabel Bravo"], date=datetime(2024, 2, 27), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/medioambiente/2024/05",
        url_normalized="https://cubadebate.cu/medioambiente/2024/05",
        title="Reciclaje se implementa en ciudades",
        content="Programas de reciclaje se están implementando en las principales ciudades del país. Los ciudadanos participan en la separación de residuos. Las autoridades han instalado puntos de acopio en neighborhoods.",
        authors=["Manuel Solís"], date=datetime(2024, 3, 8), indexed=False, embeddings_generated=False
    ),
    
    # Internacionales
    ScrapedDocument(
        source="telecentros", url="https://telecentros.cu/noticias/2024/01",
        url_normalized="https://telecentros.cu/noticias/2024/01",
        title="Cumbre mundial aborda crisis climática",
        content="Una cumbre mundial se reúne para abordar la crisis climática global. Líderes de países discuten acuerdos para reducir las emisiones de gases de efecto invernadero. Los activistas طلب more ambitious metas.",
        authors=["Teresa Arrieta"], date=datetime(2024, 1, 12), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="telecentros", url="https://telecentros.cu/noticias/2024/02",
        url_normalized="https://telecentros.cu/noticias/2024/02",
        title="Acuerdo comercial entre países latinoamericanos",
        content="Países latinoamericanos firman un nuevo acuerdo comercial para promover el intercambio de bienes y servicios. El pacto busca fortalecer la integración regional. Los empresarios esperan beneficiarse del mercado común.",
        authors=["Antonio Medina"], date=datetime(2024, 1, 19), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="telecentros", url="https://telecentros.cu/noticias/2024/03",
        url_normalized="https://telecentros.cu/noticias/2024/03",
        title="Conflicto internacional genera tensiones",
        content="Un conflicto internacional ha generado tensiones en diversas regiones del mundo. Las potencias mundiales discuten soluciones diplomáticas. Los efectos económicos se sienten en los mercados globales.",
        authors=["Carmen navarro"], date=datetime(2024, 2, 4), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="telecentros", url="https://telecentros.cu/noticias/2024/04",
        url_normalized="https://telecentros.cu/noticias/2024/04",
        title="Organismos internacionales aiden a países pobres",
        content="Organismos internacionales envían ayuda humanitaria a países que sufren crisis alimentarias. Los programas de asistencia incluyen alimentos, medicinas y agua potable. Millones de personas dependen de esta ayuda.",
        authors=["Roberto Castillo"], date=datetime(2024, 2, 13), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="telecentros", url="https://telecentros.cu/noticias/2024/05",
        url_normalized="https://telecentros.cu/noticias/2024/05",
        title="Migración masiva hacia países desarrollados",
        content="La migración masiva continúa hacia países desarrollados. Miles de personas buscan mejores oportunidades laborales y de vida. Los gobiernos debaten políticas migratorias más estrictas.",
        authors=["Patricia fuentes"], date=datetime(2024, 2, 21), indexed=False, embeddings_generated=False
    ),
    
    # Sociedad
    ScrapedDocument(
        source="radiorebelde", url="https://radiorebelde.cu/sociedad/2024/01",
        url_normalized="https://radiorebelde.cu/sociedad/2024/01",
        title="Educación universitaria es gratuita",
        content="La educación universitaria sigue siendo gratuita en el país. Miles de jóvenes acceden a la enseñanza superior cada año. Las universidades ofrecen carreras en diversas áreas del conocimiento.",
        authors=["JaimeEscobar"], date=datetime(2024, 1, 16), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="radiorebelde", url="https://radiorebelde.cu/sociedad/2024/02",
        url_normalized="https://radiorebelde.cu/sociedad/2024/02",
        title="Vivienda para familias de bajos recursos",
        content="El gobierno construye viviendas para familias de bajos recursos económicos. Los beneficiarios reciben casas con todas las comodidades básicas. El programa de vivienda ha mejorado la calidad de vida de miles de familias.",
        authors=["Margarita Duffy"], date=datetime(2024, 1, 26), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="radiorebelde", url="https://radiorebelde.cu/sociedad/2024/03",
        url_normalized="https://radiorebelde.cu/sociedad/2024/03",
        title="Seguridad social cubre a adultos mayores",
        content="El sistema de seguridad social cubre a los adultos mayores del país. Los pensionados reciben ayudas económicas mensuales. Los servicios de salud geriátrica han sido ampliados.",
        authors=["René Montoya"], date=datetime(2024, 2, 4), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="radiorebelde", url="https://radiorebelde.cu/sociedad/2024/04",
        url_normalized="https://radiorebelde.cu/sociedad/2024/04",
        title="Mujeres ocupan cargos de dirección",
        content="Las mujeres ocupan cada vez más cargos de dirección en la sociedad. Las políticas de igualdad de género han dado resultados positivos. Más mujeres líderes contribuyen al desarrollo del país.",
        authors=["Silvia Zambrano"], date=datetime(2024, 2, 23), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="radiorebelde", url="https://radiorebelde.cu/sociedad/2024/05",
        url_normalized="https://radiorebelde.cu/sociedad/2024/05",
        title="Juventud participa en programas sociales",
        content="La juventud participa activamente en programas sociales y comunitarios. Los estudiantes realizan actividades de voluntariado en neighborhoods marginados. Estas experiencias forman ciudadanos comprometidos.",
        authors=["Ernesto Páez"], date=datetime(2024, 3, 6), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/politica/2024/01",
        url_normalized="cubadebate_cu_politica_2024_01",
        title="Gobierno de Cuba celebra anniversary de revolución",
        content="El gobierno de Cuba celebró el aniversario de la revolución cubana. Miles de personas salieron a las calles de La Habana para commemorar la fecha histórica. El presidente destacó los logros de la revolución en educación y salud.",
        authors=["Editorial"], date=datetime(2024, 1, 1), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/politica/2024/02",
        url_normalized="cubadebate_cu_politica_2024_02",
        title="Cuba fortalece relaciones diplomáticas con países del ALBA",
        content="Cuba fortalece sus relaciones diplomáticas con países vecinos del ALBA. Se han firmado nuevos acuerdos de cooperación en áreas como comercio, cultura y educación. Los embajadores han destacado la importancia del diálogo regional.",
        authors=["Juan Pérez"], date=datetime(2024, 2, 15), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/deportes/2024/01",
        url_normalized="cubadebate_cu_deportes_2024_01",
        title="Boxeo cubano mantiene hegemonía en Juegos del Caribe",
        content="El boxeo cubano mantiene su hegemonía en los Juegos del Caribe. Los boxeadores cubanos han conquistado oro en diversas categorías. Los expertos consideran que Cuba sigue siendo una potencia mundial del boxeo amateur.",
        authors=["Carlos López"], date=datetime(2024, 1, 20), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/salud/2024/01",
        url_normalized="cubadebate_cu_salud_2024_01",
        title="Médicos cubanos colaboran en programas de salud en África",
        content="Médicos cubanos continúan colaborando en programas de salud en el exterior. Brigadas médicas han sido enviadas a países de África y América Latina. Los profesionales de la salud han recibido reconocimientos internacionales.",
        authors=["Patricia Reyes"], date=datetime(2024, 2, 12), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/economia/2024/01",
        url_normalized="cubadebate_cu_economia_2024_01",
        title="Economía cubana enfrenta desafíos en 2024",
        content="La economía cubana enfrenta desafíos significativos en 2024. El gobierno ha implementado nuevas medidas para estimular la producción nacional. Los analistas económicos discuten el futuro del modelo cubano.",
        authors=["María García"], date=datetime(2024, 3, 1), indexed=False, embeddings_generated=False
    ),
    
    # ===== MÉXICO =====
    ScrapedDocument(
        source="elnacional", url="https://www.elnacional.mx/mexico/2024/01",
        url_normalized="elnacional_mx_mexico_2024_01",
        title="México firma acuerdos comerciales con países de América Latina",
        content="México firma nuevos acuerdos comerciales con países de América Latina. El presidente mexicano viajó a Argentina y Brasil para fortalecer las relaciones económicas. Los tratados incluyen intercambio de productos agrícolas y tecnología.",
        authors=["Ana Martínez"], date=datetime(2024, 1, 15), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="elnacional", url="https://www.elnacional.mx/mexico/2024/02",
        url_normalized="elnacional_mx_mexico_2024_02",
        title="Sistema de salud mexicano mejora infraestructura hospitalaria",
        content="El sistema de salud mexicano invierte en nueva infraestructura hospitalaria. Se han construido hospitales en estados del sur del país. Los médicos mexicanos han recibido capacitación especializada.",
        authors=["Roberto Castillo"], date=datetime(2024, 2, 8), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="elnacional", url="https://www.elnacional.mx/mexico/2024/03",
        url_normalized="elnacional_mx_mexico_2024_03",
        title="Selección mexicana de fútbol clasifica al mundial",
        content="La selección mexicana de fútbol ha clasificado al mundial después de un intenso partido contra Estados Unidos. Los goles fueron marcados por delanteros mexicanos. Los aficionados celebran en las calles de Ciudad de México.",
        authors=["Pedro Sánchez"], date=datetime(2024, 3, 10), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="elnacional", url="https://www.elnacional.mx/mexico/2024/04",
        url_normalized="elnacional_mx_mexico_2024_04",
        title="Relaciones México-Cuba fortalecen intercambio cultural",
        content="Las relaciones entre México y Cuba se han fortalecido en materia cultural. Artistas mexicanos han participado en festivales en La Habana. El intercambio de música y cine beneficia a ambos países.",
        authors=["Laura Rodríguez"], date=datetime(2024, 2, 25), indexed=False, embeddings_generated=False
    ),
    
    # ===== ARGENTINA =====
    ScrapedDocument(
        source="lanacion", url="https://www.lanacion.com.ar/argentina/2024/01",
        url_normalized="lanacion_ar_argentina_2024_01",
        title="Argentina negocia deuda con el Fondo Monetario Internacional",
        content="Argentina continúa negociando la deuda con el Fondo Monetario Internacional. El ministro de economía se reunió con funcionarios del FMI en Washington. Se discuten nuevas condiciones para el pago de la deuda argentina.",
        authors=["Roberto Díaz"], date=datetime(2024, 1, 18), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="lanacion", url="https://www.lanacion.com.ar/argentina/2024/02",
        url_normalized="lanacion_ar_argentina_2024_02",
        title="Selección argentina de fútbol enfrenta a Brasil en eliminatorias",
        content="La selección argentina de fútbol se enfrenta a Brasil en las eliminatorias sudamericanas. Lionel Messi liderará el equipo argentino. Los partidos se jugarán en Buenos Aires y Río de Janeiro.",
        authors=["Sofia Hernández"], date=datetime(2024, 2, 20), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="lanacion", url="https://www.lanacion.com.ar/argentina/2024/03",
        url_normalized="lanacion_ar_argentina_2024_03",
        title="Economía argentina muestra signos de recuperación",
        content="La economía argentina muestra signos de recuperación después de meses de crisis. El tipo de cambio se ha estabilizado y la inflación ha disminuido. Los economistas debaten sobre las perspectivas futuras.",
        authors=["Miguel Fernández"], date=datetime(2024, 3, 5), indexed=False, embeddings_generated=False
    ),
    
    # ===== VENEZUELA =====
    ScrapedDocument(
        source="eluniversal", url="https://www.eluniversal.com.ve/venezuela/2024/01",
        url_normalized="eluniversal_ve_venezuela_2024_01",
        title="Venezuela firma acuerdos petroleros con países de la OPEP",
        content="Venezuela firma nuevos acuerdos petroleros con países miembros de la OPEP. Las negociaciones incluyen a Arabia Saudita y Rusia. El petróleo venezolano es clave para la economía del país.",
        authors=["Elena Vargas"], date=datetime(2024, 1, 22), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="eluniversal", url="https://www.eluniversal.com.ve/venezuela/2024/02",
        url_normalized="eluniversal_ve_venezuela_2024_02",
        title="Sistema de salud venezolano requiere inversiones urgentes",
        content="El sistema de salud venezolano enfrenta crisis y requiere inversiones urgentes. Médicos venezolanos han emigrado a otros países buscando mejores condiciones. La Organización Mundial de la Salud ha alertado sobre la situación.",
        authors=["Jorge Morales"], date=datetime(2024, 2, 14), indexed=False, embeddings_generated=False
    ),
    
    # ===== BOLIVIA =====
    ScrapedDocument(
        source="eldeber", url="https://eldeber.com.bo/bolivia/2024/01",
        url_normalized="eldeber_bo_bolivia_2024_01",
        title="Bolivia desarrolla industria del litio para exportar",
        content="Bolivia desarrolla su industria del litio para exportar a mercados internacionales. El país posee las mayores reservas de litio del mundo. Empresas de China y Estados Unidos han mostrado interés en invertir.",
        authors=["Patricia Reyes"], date=datetime(2024, 1, 30), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="eldeber", url="https://eldeber.com.bo/bolivia/2024/02",
        url_normalized="eldeber_bo_bolivia_2024_02",
        title="Fútbol boliviano busca clasificatoria al mundial",
        content="La selección boliviana de fútbol busca clasificatoria al mundial. Los partidos de eliminatorias se juegan en La Paz a gran altura. El cuerpo técnico ha convocado a nuevos jugadores.",
        authors=["Andrés Castro"], date=datetime(2024, 2, 18), indexed=False, embeddings_generated=False
    ),
    
    # ===== BRASIL =====
    ScrapedDocument(
        source="folha", url="https://www.folha.com.br/brasil/2024/01",
        url_normalized="folha_br_brasil_2024_01",
        title="Brasil lidera producción agrícola en América del Sur",
        content="Brasil lidera la producción agrícola en América del Sur. Las exportaciones de soja y carne han aumentado significativamente. El sector agrícola representa una parte importante de la economía brasileña.",
        authors=["Lucía Méndez"], date=datetime(2024, 2, 25), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="folha", url="https://www.folha.com.br/brasil/2024/02",
        url_normalized="folha_br_brasil_2024_02",
        title="Selección brasileira de fútbol prepara班上 para Copa América",
        content="La selección brasileña de fútbol se prepara para la Copa América. El entrenador ha convocado a estrellas del fútbol brasileiro. Los partidos se jugarán en Estados Unidos.",
        authors=["Raúl Ortega"], date=datetime(2024, 3, 8), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="folha", url="https://www.folha.com.br/brasil/2024/03",
        url_normalized="folha_br_brasil_2024_03",
        title="Brasil y China firman acuerdos de cooperación tecnológica",
        content="Brasil y China firman acuerdos de cooperación tecnológica. Las inversiones incluyen desarrollo de inteligencia artificial y energía renovable. El intercambio comercial entre ambos países ha crecido.",
        authors=["Diana Flores"], date=datetime(2024, 2, 6), indexed=False, embeddings_generated=False
    ),
    
    # ===== COLOMBIA =====
    ScrapedDocument(
        source="eltiempo", url="https://www.eltiempo.com/colombia/2024/01",
        url_normalized="eltiempo_co_colombia_2024_01",
        title="Proceso de paz en Colombia avanza con nuevas negociaciones",
        content="El proceso de paz en Colombia avanza con nuevas negociaciones con grupos armados. El gobierno ha iniciado diálogos de paz. Los acuerdos incluyen desarme y reinserción social.",
        authors=["Gustavo Peña"], date=datetime(2024, 2, 14), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="eltiempo", url="https://www.eltiempo.com/colombia/2024/02",
        url_normalized="eltiempo_co_colombia_2024_02",
        title="Café colombiano mantiene liderazgo en exportaciones",
        content="El café colombiano mantiene su liderazgo en exportaciones mundiales. Los productores han mejorado técnicas de cultivo. El grano colombiano es reconocido por su alta calidad.",
        authors=["Hugo Jiménez"], date=datetime(2024, 2, 22), indexed=False, embeddings_generated=False
    ),
    
    # ===== PERÚ =====
    ScrapedDocument(
        source="larepublica", url="https://larepublica.pe/peru/2024/01",
        url_normalized="larepublica_pe_peru_2024_01",
        title="Perú enfrenta desafíos en sector minero",
        content="Perú enfrenta desafíos en el sector minero por conflictos sociales. Las exportaciones mineras son fundamentales para la economía. El gobierno busca diálogo con comunidades afectadas.",
        authors=["Marta Delgado"], date=datetime(2024, 3, 5), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="larepublica", url="https://larepublica.pe/peru/2024/02",
        url_normalized="larepublica_pe_peru_2024_02",
        title="Gastronomía peruana reconocida mundialmente",
        content="La gastronomía peruana ha sido reconocida mundialmente con premios internacionales. Restaurantes peruanos lideran rankings en América Latina. El cebiche y la causa son platos emblemáticos.",
        authors=["Claudia Ruiz"], date=datetime(2024, 1, 28), indexed=False, embeddings_generated=False
    ),
    
    # ===== CHILE =====
    ScrapedDocument(
        source="latercera", url="https://www.latercera.com/chile/2024/01",
        url_normalized="latercera_cl_chile_2024_01",
        title="Chile lidera en producción de cobre a nivel mundial",
        content="Chile lidera la producción de cobre a nivel mundial. Las minas de cobre representan la principal fuente de ingresos del país. Empresas mineras han invertido en tecnología de extracción.",
        authors=["Fernando Soto"], date=datetime(2024, 2, 7), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="latercera", url="https://www.latercera.com/chile/2024/02",
        url_normalized="latercera_cl_chile_2024_02",
        title="Chile implementa políticas de energía renovable",
        content="Chile implementa políticas de energía renovable a gran escala. El país ha invertido en paneles solares y energía eólica. Las metas incluyen carbono neutralidad para 2050.",
        authors=["Rosa Vázquez"], date=datetime(2024, 2, 16), indexed=False, embeddings_generated=False
    ),
    
    # ===== ESTADOS UNIDOS =====
    ScrapedDocument(
        source="nytimes", url="https://www.nytimes.com/us/2024/01",
        url_normalized="nytimes_com_us_2024_01",
        title="Estados Unidos anuncia nuevas políticas migratorias",
        content="Estados Unidos anuncia nuevas políticas migratorias para controlar la frontera sur. La medida ha generado debate en el congreso. Inmigrantes de países centroamericanos buscan asilo.",
        authors=["Alberto Romero"], date=datetime(2024, 2, 24), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="nytimes", url="https://www.nytimes.com/us/2024/02",
        url_normalized="nytimes_com_us_2024_02",
        title="Tecnología de inteligencia artificial lidera inversiones en USA",
        content="La tecnología de inteligencia artificial lidera las inversiones en Estados Unidos. Empresas como Google y Microsoft han invertido miles de millones. El desarrollo de IA transforma múltiples sectores.",
        authors=["Gloria Ibarra"], date=datetime(2024, 3, 3), indexed=False, embeddings_generated=False
    ),
    
    # ===== CHINA =====
    ScrapedDocument(
        source="scmp", url="https://www.scmp.com/china/2024/01",
        url_normalized="scmp_com_china_2024_01",
        title="China desarrolla tecnología 5G en toda Asia",
        content="China desarrolla tecnología 5G en toda Asia con inversiones masivas. Las empresas tecnológicas chinas lideran el despliegue de redes. El 5G transformará la comunicación móvil.",
        authors=["Ricardo Peña"], date=datetime(2024, 1, 30), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="scmp", url="https://www.scmp.com/china/2024/02",
        url_normalized="scmp_com_china_2024_02",
        title="China firma acuerdos comerciales con países de África",
        content="China firma acuerdos comerciales con países de África para expandir su influencia. Las inversiones incluyen infraestructura y recursos naturales. El comercio sino-africano ha crecido significativamente.",
        authors=["Sandra Mendoza"], date=datetime(2024, 2, 9), indexed=False, embeddings_generated=False
    ),
    
    # ===== SALUD GLOBAL =====
    ScrapedDocument(
        source="who", url="https://www.who.int/salud/2024/01",
        url_normalized="who_int_salud_2024_01",
        title="Organización Mundial de la Salud advierte sobre nuevas pandemias",
        content="La Organización Mundial de la Salud advierte sobre el riesgo de nuevas pandemias. Países de todo el mundo deben fortalecer sus sistemas de salud. Los médicos y enfermeras son fundamentales en la respuesta.",
        authors=["Óscar Ramírez"], date=datetime(2024, 2, 17), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="who", url="https://www.who.int/salud/2024/02",
        url_normalized="who_int_salud_2024_02",
        title="Vacunas contra enfermedades tropicales en desarrollo",
        content="Investigadores trabajan en nuevas vacunas contra enfermedades tropicales. Los laboratorios han recibido financiamiento de gobiernos y organizaciones. La malaria y el dengue son prioritarios.",
        authors=["Verónica Luna"], date=datetime(2024, 2, 26), indexed=False, embeddings_generated=False
    ),
    
    # ===== ECONOMÍA GLOBAL =====
    ScrapedDocument(
        source="bbc", url="https://www.bbc.com/economia/2024/01",
        url_normalized="bbc_com_economia_2024_01",
        title="Economía global enfrenta incertidumbre por inflación",
        content="La economía global enfrenta incertidumbre por la inflación persistente. Bancos centrales han subido tasas de interés. Los analistas discuten sobre una posible recesión mundial.",
        authors=["Daniel Herrera"], date=datetime(2024, 3, 7), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="bbc", url="https://www.bbc.com/economia/2024/02",
        url_normalized="bbc_com_economia_2024_02",
        title="Comercio internacional se recupera lentamente",
        content="El comercio internacional se recupera lentamente después de la pandemia. Los tratados comerciales facilitan el intercambio entre países. El transporte marítimo ha aumentado.",
        authors=["Eugenio Guzmán"], date=datetime(2024, 2, 2), indexed=False, embeddings_generated=False
    ),
    
    # ===== TECNOLOGÍA =====
    ScrapedDocument(
        source="techcrunch", url="https://techcrunch.com/tecnologia/2024/01",
        url_normalized="techcrunch_com_tecnologia_2024_01",
        title="Startups de inteligencia artificial atraen inversiones récord",
        content="Startups de inteligencia artificial atraen inversiones récord en Silicon Valley. Los fundadores han desarrollado nuevos modelos de lenguaje. La inteligencia artificial está transformando la industria tecnológica.",
        authors=["Beatriz Pardo"], date=datetime(2024, 2, 11), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="techcrunch", url="https://techcrunch.com/tecnologia/2024/02",
        url_normalized="techcrunch_com_tecnologia_2024_02",
        title="Ciberseguridad: empresas invierten contra ataques informáticos",
        content="Empresas de ciberseguridad informan sobre aumento de ataques informáticos. Los hackers han targeting sistemas de países y empresas. La inversión en ciberseguridad ha crecido significativamente.",
        authors=["Francisco Leiva"], date=datetime(2024, 2, 19), indexed=False, embeddings_generated=False
    ),
    
    # ===== DEPORTES VARIOS =====
    ScrapedDocument(
        source="espn", url="https://www.espn.com/deportes/2024/01",
        url_normalized="espn_com_deportes_2024_01",
        title="Copa América 2024: equipos sudamericanos se preparan",
        content="Equipos sudamericanos se preparan para la Copa América 2024. Brasil, Argentina, Uruguay y Colombia buscan el título. Los estadios en Estados Unidos albergará los partidos.",
        authors=["Isabel Bravo"], date=datetime(2024, 2, 27), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="espn", url="https://www.espn.com/deportes/2024/02",
        url_normalized="espn_com_deportes_2024_02",
        title="Atletas latinoamericanos destacan en Juegos Olímpicos juveniles",
        content="Atletas latinoamericanos destacan en los Juegos Olímpicos juveniles. Mexicoños, brasileños y colombianos han ganado medallas. El atletismo y la natación son deportes destacados.",
        authors=["Manuel Solís"], date=datetime(2024, 3, 8), indexed=False, embeddings_generated=False
    ),
    
    # ===== CULTURA =====
    ScrapedDocument(
        source="cultura", url="https://www.cultura.com/latinoamerica/2024/01",
        url_normalized="cultura_com_latinoamerica_2024_01",
        title="Arte latinoamericano expuesto en museos de Europa",
        content="Arte latinoamericano expone en museos de Europa con gran éxito. Pintores de México, Argentina y Brasil son destacados. Las exposiciones incluyen arte precolombino y contemporáneo.",
        authors=["Teresa Arrieta"], date=datetime(2024, 1, 12), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cultura", url="https://www.cultura.com/latinoamerica/2024/02",
        url_normalized="cultura_com_latinoamerica_2024_02",
        title="Música latina domina listas de popularidad mundiales",
        content="La música latina domina las listas de popularidad mundiales. Artistas de Colombia, México y Argentina lideran rankings. El reggaetón y la bachata son géneros populares.",
        authors=["Antonio Medina"], date=datetime(2024, 2, 4), indexed=False, embeddings_generated=False
    ),
    
    # ===== EDUCACIÓN =====
    ScrapedDocument(
        source="educacion", url="https://www.educacion.com/america/2024/01",
        url_normalized="educacion_com_america_2024_01",
        title="Universidades latinoamericanas ranking en investigación",
        content="Universidades latinoamericanas mejoran su ranking en investigación científica. Brasil, México y Argentina lideran en publicaciones. Los doctores e investigadores son formados en estas instituciones.",
        authors=["Carmen Navarro"], date=datetime(2024, 2, 4), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="educacion", url="https://www.educacion.com/america/2024/02",
        url_normalized="educacion_com_america_2024_02",
        title="Becas internacionales para estudiantes de América Latina",
        content="Becas internacionales ofrecen oportunidades para estudiantes de América Latina. Programas de España, Estados Unidos y China están disponibles. Los estudiantes pueden estudiar en el exterior con financiamiento.",
        authors=["Roberto Castillo"], date=datetime(2024, 2, 13), indexed=False, embeddings_generated=False
    ),
    
    # ===== MÁS CUBA =====
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/turismo/2024/01",
        url_normalized="cubadebate_cu_turismo_2024_01",
        title="Turismo en Cuba se recupera lentamente",
        content="El turismo en Cuba se recupera lentamente después de la pandemia. Hoteles en La Habana y Varadero reciben visitantes internacionales. El gobierno ha invertido en infraestructura turística.",
        authors=["Patricia Fuentes"], date=datetime(2024, 2, 21), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/cultura/2024/01",
        url_normalized="cubadebate_cu_cultura_2024_01",
        title="Música cubana reconocida internacionalmente",
        content="La música cubana sigue siendo reconocida internacionalmente. Artistas de salsa y son cubano han tocado en festivales mundiales. La cultura cubana influye en la música latinoamericana.",
        authors=["Jaime Escobar"], date=datetime(2024, 1, 16), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="cubadebate", url="https://cubadebate.cu/educacion/2024/01",
        url_normalized="cubadebate_cu_educacion_2024_01",
        title="Sistema educativo cubano: logros y desafíos",
        content="El sistema educativo cubano ha logrado altos niveles de alfabetización. Estudiantes cubanos han participado en olimpiadas internacionales de matemáticas. Los desafíos incluyen recursos materiales.",
        authors=["Margarita Duffy"], date=datetime(2024, 1, 26), indexed=False, embeddings_generated=False
    ),
    
    # ===== MÁS MÉXICO =====
    ScrapedDocument(
        source="elnacional", url="https://www.elnacional.mx/mexico/2024/05",
        url_normalized="elnacional_mx_mexico_2024_05",
        title="Amlo analiza relaciones con Estados Unidos sobre migración",
        content="El presidente de México analiza las relaciones con Estados Unidos sobre el tema migratorio. Ambos países discuten políticas para controlar la migración irregular. Acuerdos bilaterales son necesarios.",
        authors=["René Montoya"], date=datetime(2024, 2, 4), indexed=False, embeddings_generated=False
    ),
    ScrapedDocument(
        source="elnacional", url="https://www.elnacional.mx/mexico/2024/06",
        url_normalized="elnacional_mx_mexico_2024_06",
        title="Tequila mexicano: patrimonio cultural y exportación",
        content="El tequila mexicano es reconocido como patrimonio cultural. Las exportaciones de tequila a Estados Unidos y Europa han aumentado. El agave azul es cultivado en Jalisco.",
        authors=["Silvia Zambrano"], date=datetime(2024, 2, 23), indexed=False, embeddings_generated=False
    ),
    
    # ===== VARIOS =====
    ScrapedDocument(
        source="varios", url="https://www.varios.com/politica/2024/01",
        url_normalized="varios_com_politica_2024_01",
        title="Gobiernos latinoamericanos firman декларация de unidad",
        content="Gobiernos latinoamericanos firman declaración de unidad para enfrentar desafíos comunes. Países de América del Sur y Central participan. Los acuerdos incluyen comercio y seguridad regional.",
        authors=["Ernesto Páez"], date=datetime(2024, 3, 6), indexed=False, embeddings_generated=False
    )
]
    
    await index_service.index_scraped_documents(scraped_docs)
    print("✅ Indexación completada")

if __name__ == "__main__":
    asyncio.run(main())
