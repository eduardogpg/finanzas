from django.db import models
from django.utils.translation import gettext_lazy as _

from prospects.models import Prospect

class Address(models.Model):
    
    class STATES(models.TextChoices):
        CHIAPAS = 'Chiapas', _('Chiapas')


    class TOWNSHIPS(models.TextChoices):
        ACACOYAGUA = 'Acacoyagua', _('Acacoyagua'),
        ACALA = 'Acala', _('Acala'),
        ACAPETAHUA = 'Acapetahua', _('Acapetahua'),
        ALTAMIRANO = 'Altamirano', _('Altamirano'),
        AMATAN = 'Amatán', _('Amatán'),
        AMATENANGO_DE_LA_FRONTERA = 'Amatenango de la Frontera', _('Amatenango de la Frontera'),
        AMATENANGO_DEL_VALLE = 'Amatenango del Valle', _('Amatenango del Valle'),
        ANGEL_ALBINO_CORZO = 'Angel Albino Corzo', _('Angel Albino Corzo'),
        ARRIAGA = 'Arriaga', _('Arriaga'),
        BEJUCALDE_OCAMPO = 'Bejucalde Ocampo', _('Bejucalde Ocampo'),
        BELLAVISTA = 'Bella Vista', _('Bella Vista'),
        BERRIOZABAL = 'Berriozábal', _('Berriozábal'),
        BOCHIL = 'Bochil', _('Bochil'),
        ELBOSQUE = 'ElBosque', _('ElBosque'),
        CACAHOATAN = 'Cacahoatán', _('Cacahoatán'),
        CATAZAJA = 'Catazajá', _('Catazajá'),
        CINTALAPA = 'Cintalapa', _('Cintalapa'),
        COAPILLA = 'Coapilla', _('Coapilla'),
        COMITAN_DE_DOMÍNGUEZ = 'Comitán de Domínguez', _('Comitán de Domínguez'),
        LACONCORDIA = 'LaConcordia', _('LaConcordia'),
        COPAINALA = 'Copainalá', _('Copainalá'),
        CHALCHIHUITAN = 'Chalchihuitán', _('Chalchihuitán'),
        CHAMULA = 'Chamula', _('Chamula'),
        CHANAL = 'Chanal', _('Chanal'),
        CHAPULTENANGO = 'Chapultenango', _('Chapultenango'),
        CHENALHO = 'Chenalhó', _('Chenalhó'),
        CHIAPA_DE_CORZO = 'Chiapa de Corzo', _('Chiapade Corzo'),
        CHIAPILLA = 'Chiapilla', _('Chiapilla'),
        CHICOASEN = 'Chicoasén', _('Chicoasén'),
        CHICOMUSELO = 'Chicomuselo', _('Chicomuselo'),
        CHILON = 'Chilón', _('Chilón'),
        ESCUINTLA = 'Escuintla', _('Escuintla'),
        FRANCISCO_LEON = 'Francisco León', _('Francisco León'),
        FRONTERA_COMALAPA = 'Frontera Comalapa', _('Frontera Comalapa'),
        FRONTERA_HIDALGO = 'Frontera Hidalgo', _('Frontera Hidalgo'),
        LAGRANDEZA = 'LaGrandeza', _('LaGrandeza'),
        HUEHUETAN = 'Huehuetán', _('Huehuetán'),
        HUIXTAN = 'Huixtán', _('Huixtán'),
        HUITIUPAN = 'Huitiupán', _('Huitiupán'),
        HUIXTLA = 'Huixtla', _('Huixtla'),
        LAINDEPENDENCIA = 'La Independencia', _('La Independencia'),
        IXHUATAN = 'Ixhuatán', _('Ixhuatán'),
        IXTACOMITAN = 'Ixtacomitán', _('Ixtacomitán'),
        IXTAPA = 'Ixtapa', _('Ixtapa'),
        IXTAPANGAJOYA = 'Ixtapangajoya', _('Ixtapangajoya'),
        JIQUIPILAS = 'Jiquipilas', _('Jiquipilas'),
        JITOTOL = 'Jitotol', _('Jitotol'),
        JUAREZ = 'Juárez', _('Juárez'),
        LARRAINZAR = 'Larráinzar', _('Larráinzar'),
        LALIBERTAD = 'LaLibertad', _('LaLibertad'),
        MAPASTEPEC = 'Mapastepec', _('Mapastepec'),
        LAS_MARGARITAS = 'Las Margaritas', _('Las Margaritas'),
        MAZAPADE_MADERO = 'Mazapade Madero', _('Mazapade Madero'),
        MAZATAN = 'Mazatán', _('Mazatán'),
        METAPA = 'Metapa', _('Metapa'),
        MITONTIC = 'Mitontic', _('Mitontic'),
        MOTOZINTLA = 'Motozintla', _('Motozintla'),
        NICOLASRUIZ = 'NicolásRuíz', _('NicolásRuíz'),
        OCOSINGO = 'Ocosingo', _('Ocosingo'),
        OCOTEPEC = 'Ocotepec', _('Ocotepec'),
        OCOZOCOAUTLADE_ESPINOSA = 'Ocozocoautla de Espinosa', _('Ocozocoautla de Espinosa'),
        OSTUACAN = 'Ostuacán', _('Ostuacán'),
        OSUMACINTA = 'Osumacinta', _('Osumacinta'),
        OXCHUC = 'Oxchuc', _('Oxchuc'),
        PALENQUE = 'Palenque', _('Palenque'),
        PANTELHO = 'Pantelhó', _('Pantelhó'),
        PANTEPEC = 'Pantepec', _('Pantepec'),
        PICHUCALCO = 'Pichucalco', _('Pichucalco'),
        PIJIJIAPAN = 'Pijijiapan', _('Pijijiapan'),
        ELPORVENIR = 'El Porvenir', _('El Porvenir'),
        VILLACOMALTITLAN = 'Villa Comaltitlán', _('Villa Comaltitlán'),
        PUEBLO_NUEVO_SOLISTAHUACAN = 'Pueblo Nuevo Solistahuacán', _('Pueblo Nuevo Solistahuacán'),
        RAYON = 'Rayón', _('Rayón'),
        REFORMA = 'Reforma', _('Reforma'),
        LASROSAS = 'LasRosas', _('LasRosas'),
        SABANILLA = 'Sabanilla', _('Sabanilla'),
        SALTO_DEAGUA = 'Salto deAgua', _('Salto deAgua'),
        SAN_CRISTOBAL_DE_LAS_CASAS = 'San Cristóbal de las Casas', _('SanCristóbal de las Casas'),
        SANFERNANDO = 'SanFernando', _('SanFernando'),
        SILTEPEC = 'Siltepec', _('Siltepec'),
        SIMOJOVEL = 'Simojovel', _('Simojovel'),
        SITALA = 'Sitalá', _('Sitalá'),
        SOCOLTENANGO = 'Socoltenango', _('Socoltenango'),
        SOLOSUCHIAPA = 'Solo suchiapa', _('Solo suchiapa'),
        SOYALO = 'Soyaló', _('Soyaló'),
        SUCHIAPA = 'Suchiapa', _('Suchiapa'),
        SUCHIATE = 'Suchiate', _('Suchiate'),
        SUNUAPA = 'Sunuapa', _('Sunuapa'),
        TAPACHULA = 'Tapachula', _('Tapachula'),
        TAPALAPA = 'Tapalapa', _('Tapalapa'),
        TAPILULA = 'Tapilula', _('Tapilula'),
        TECPATAN = 'Tecpatán', _('Tecpatán'),
        TENEJAPA = 'Tenejapa', _('Tenejapa'),
        TEOPISCA = 'Teopisca', _('Teopisca'),
        TILA = 'Tila', _('Tila'),
        TONALA = 'Tonalá', _('Tonalá'),
        TOTOLAPA = 'Totolapa', _('Totolapa'),
        LATRINITARIA = 'LaTrinitaria', _('LaTrinitaria'),
        TUMBALA = 'Tumbalá', _('Tumbalá'),
        TUXTLA_GUTIÉRREZ = 'Tuxtla Gutiérrez', _('Tuxtla Gutiérrez'),
        TUXTLA_CHICO = 'Tuxtla Chico', _('Tuxtla Chico'),
        TUZANTAN = 'Tuzantán', _('Tuzantán'),
        TZIMOL = 'Tzimol', _('Tzimol'),
        UNION_JUAREZ = 'UniónJuárez', _('UniónJuárez'),
        VENUSTIANO_CARRANZA = 'Venustiano Carranza', _('Venustiano Carranza'),
        VILLACORZO = 'VillaCorzo', _('VillaCorzo'),
        VILLAFLORES = 'Villaflores', _('Villaflores'),
        YAJALON = 'Yajalón', _('Yajalón'),
        SANLUCAS = 'San Lucas', _('San Lucas'),
        ZINACANTAN = 'Zinacantán', _('Zinacantán'),
        SAN_JUANCANCUC = 'San JuanCancuc', _('San JuanCancuc'),
        ALDAMA = 'Aldama', _('Aldama'),
        BENEMERITODE_LAS_AMERICAS = 'Benemérito de las Américas', _('Benemérit ode las Américas'),
        MARAVILLATENEJAPA = 'Maravilla Tenejapa', _('Maravilla Tenejapa'),
        MARQUESDE_COMILLAS = 'Marquésde Comillas', _('Marquésde Comillas'),
        MONTECRISTO_DE_GUERRERO = 'Montecristo de Guerrero', _('Montecristo de Guerrero'),
        SAN_ANDRES_DURAZNAL = 'San Andrés Duraznal', _('SanAndrés Duraznal'),
        SANTIAGOEL_PINAR = 'Santiago el Pinar', _('Santiagoel Pinar'),
        CAPITAN_LUIS_ANGEL_VIDAL = 'Capitán Luis Angel Vidal', _('Capitán Luis Angel Vidal'),
        RINCONCHAMULA_SAN_PEDRO = 'Rincón Chamula San Pedro', _('Rincón Chamula San Pedro'),
        ELPARRAL = 'ElParral', _('ElParral'),
        EMILIANOZAPATA = 'EmilianoZapata', _('EmilianoZapata'),
        MEZCALAPA = 'Mezcalapa', _('Mezcalapa'),
        HONDURASDE_LA_SIERRA = 'Honduras de la Sierra', _('Honduras de la Sierra')
        
        
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField(max_length=255, null=False, blank=False)
    zip = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=255, null=False, blank=False, choices=STATES.choices, default='Chiapas') 
    suburb = models.CharField(max_length=255, null=True, blank=True) # Colonia
    township = models.CharField(max_length=255, null=True, blank=True, choices=TOWNSHIPS.choices) # Ciudad/Municipio
    lat = models.IntegerField(null=True, blank=True, default=None)
    long = models.IntegerField(null=True, blank=True, default=None)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'#{self.address} - {self.township} - {self.zip} - {self.state_format}'
    
    
    @property
    def state_format(self):
        return self.state
