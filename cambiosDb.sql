
CREATE SCHEMA IF NOT EXISTS alma_union DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE alma_union;

-- =========================================================
-- TABLAS BASE: EMPRESAS / INFLUENCERS / USUARIOS
-- =========================================================
CREATE TABLE empresas (
  id_empresa INT AUTO_INCREMENT PRIMARY KEY,
  rut_empresa VARCHAR(40) NOT NULL UNIQUE,
  nombre_empresa VARCHAR(250) NOT NULL UNIQUE,
  categoria_empresa VARCHAR(100),
) ENGINE=InnoDB;

CREATE TABLE influencers (
  id_influencer INT AUTO_INCREMENT PRIMARY KEY,
  rut_influencer VARCHAR(45) NOT NULL UNIQUE,
  nombre VARCHAR(50),
  apellido_pat VARCHAR(50),
  apellido_mat VARCHAR(50),
  user_name VARCHAR(80),
  ciudad VARCHAR(120),
  sello_autenticidad BOOL,
  calificacion_promedio DECIMAL(3,2),
  categoria_influencer VARCHAR(100),
  seguidores BIGINT,
  prom_views INT
) ENGINE=InnoDB;

CREATE TABLE usuarios (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(250) NOT NULL UNIQUE,
  contrasena VARCHAR(255) NOT NULL,
  rol VARCHAR(50),
  verificado BOOL,
  imagen_perfil LONGBLOB,
  id_empresa INT NULL,
  id_influencer INT NULL,
  CONSTRAINT fk_usuarios_empresas FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT fk_usuarios_influencers FOREIGN KEY (id_influencer) REFERENCES influencers(id_influencer) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =========================================================
-- CAMPAÑAS
-- =========================================================
CREATE TABLE campanas (
  id_campana INT AUTO_INCREMENT PRIMARY KEY,
  id_empresa INT NOT NULL,
  nombre_campana VARCHAR(250),
  descripcion TEXT,
  presupuesto DECIMAL(12,2) NOT NULL,
  fecha_inicio DATE,
  hora_inicio TIME,
  fecha_fin DATE,
  hora_fin TIME,
  CONSTRAINT fk_campanas_empresas FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =========================================================
-- REDES SOCIALES
-- =========================================================
CREATE TABLE redes_sociales (
  id_red_social INT AUTO_INCREMENT PRIMARY KEY,
  id_influencer INT,
  id_empresa INT,
  plataforma VARCHAR(50),
  user_name VARCHAR(150),
  canal VARCHAR(300),
  seguidores BIGINT,
  vistas BIGINT,
  CONSTRAINT fk_redes_influencers FOREIGN KEY (id_influencer) REFERENCES influencers(id_influencer) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_redes_empresas FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =========================================================
-- MÉTRICAS HISTÓRICAS
-- =========================================================
CREATE TABLE metricas_h (
  id_metrica INT AUTO_INCREMENT PRIMARY KEY,
  id_influencer INT,
  id_empresa INT,
  titulo VARCHAR(250),
  plataforma VARCHAR(50),
  url_video VARCHAR(300),
  fecha DATE,
  seguidores BIGINT,
  vistas BIGINT,
  CONSTRAINT fk_mh_inf FOREIGN KEY (id_influencer) REFERENCES influencers(id_influencer) ON DELETE CASCADE,
  CONSTRAINT fk_mh_emp FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa) ON DELETE CASCADE
) ENGINE=InnoDB;

-- =========================================================
-- COLABORACIONES
-- =========================================================
CREATE TABLE colaboraciones (
  id_colaboracion INT AUTO_INCREMENT PRIMARY KEY,
  id_campana INT,
  titulo_campana VARCHAR(250),
  status VARCHAR(50),
  presupuesto DECIMAL(12,2),
  fecha_inicio DATE,
  hora_inicio TIME,
  fecha_fin DATE,
  hora_fin TIME,
  CONSTRAINT fk_colab_camp FOREIGN KEY (id_campana) REFERENCES campanas(id_campana) ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE colaboracion_empresas (
  id_colaboracion_empresa INT AUTO_INCREMENT PRIMARY KEY,
  id_colaboracion INT NOT NULL,
  id_empresa INT NOT NULL,
  rol_empresa ENUM('lider','participante') DEFAULT 'participante',
  aprobo TINYINT(1) DEFAULT 0,
  aprobado_por_usuario INT NULL,
  aprobado_en DATETIME NULL,
  UNIQUE KEY uq_colab_emp (id_colaboracion,id_empresa),
  CONSTRAINT fk_ce_colab FOREIGN KEY (id_colaboracion) REFERENCES colaboraciones(id_colaboracion) ON DELETE CASCADE,
  CONSTRAINT fk_ce_emp FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE colaboracion_influencers (
  id_colaboracion_influencer INT AUTO_INCREMENT PRIMARY KEY,
  id_colaboracion INT NOT NULL,
  id_influencer INT NOT NULL,
  aprobo TINYINT(1) DEFAULT 0,
  aprobado_por_usuario INT NULL,
  aprobado_en DATETIME NULL,
  UNIQUE KEY uq_colab_inf (id_colaboracion,id_influencer),
  CONSTRAINT fk_ci_colab FOREIGN KEY (id_colaboracion) REFERENCES colaboraciones(id_colaboracion) ON DELETE CASCADE,
  CONSTRAINT fk_ci_inf FOREIGN KEY (id_influencer) REFERENCES influencers(id_influencer) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE colaboracion_historial (
  id_historial INT AUTO_INCREMENT PRIMARY KEY,
  id_colaboracion INT NOT NULL,
  actor_tipo ENUM('empresa','influencer','sistema') NOT NULL,
  actor_id INT NULL,
  id_usuario INT NULL,
  estado_anterior ENUM('propuesta','aceptada','en_proceso','finalizado','cancelada') NULL,
  estado_nuevo ENUM('propuesta','aceptada','en_proceso','finalizado','cancelada') NOT NULL,
  descripcion VARCHAR(500),
  creado_en DATETIME DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_ch_colab FOREIGN KEY (id_colaboracion) REFERENCES colaboraciones(id_colaboracion) ON DELETE CASCADE
) ENGINE=InnoDB;

-- =========================================================
-- PROPUESTAS / NEGOCIACIÓN
-- =========================================================
CREATE TABLE propuestas (
  id_propuesta INT AUTO_INCREMENT PRIMARY KEY,
  id_empresa INT NOT NULL,
  id_influencer INT NOT NULL,
  id_campana INT NULL,
  id_colaboracion INT NULL,
  alcance_entregables TEXT,
  monto DECIMAL(12,2),
  plazos VARCHAR(250),
  servicios_incluidos TEXT,
  extras_resumen TEXT,
  estado ENUM('borrador','enviada','contraoferta','aceptada','rechazada','expirada') DEFAULT 'borrador',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_prop_emp FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa) ON DELETE CASCADE,
  CONSTRAINT fk_prop_inf FOREIGN KEY (id_influencer) REFERENCES influencers(id_influencer) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE propuesta_servicios (
  id_servicio INT AUTO_INCREMENT PRIMARY KEY,
  id_propuesta INT NOT NULL,
  tipo_servicio ENUM('reel','publicacion','video') NOT NULL,
  cantidad INT DEFAULT 1,
  costo_unitario DECIMAL(12,2),
  CONSTRAINT fk_ps_prop FOREIGN KEY (id_propuesta) REFERENCES propuestas(id_propuesta) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE propuesta_servicios_extras (
  id_extra INT AUTO_INCREMENT PRIMARY KEY,
  id_propuesta INT NOT NULL,
  tipo_extra ENUM('arriendo_local','arriendo_camaras','asistencia_fotografica','otro') NOT NULL,
  descripcion TEXT,
  precio DECIMAL(12,2),
  cantidad INT DEFAULT 1,
  fecha_solicitud DATE,
  CONSTRAINT fk_pse_prop FOREIGN KEY (id_propuesta) REFERENCES propuestas(id_propuesta) ON DELETE CASCADE
) ENGINE=InnoDB;

-- =========================================================
-- OPORTUNIDADES
-- =========================================================
CREATE TABLE oportunidades (
  id_oportunidad INT AUTO_INCREMENT PRIMARY KEY,
  id_empresa INT NOT NULL,
  id_campana INT NULL,
  titulo VARCHAR(200),
  descripcion TEXT,
  categoria VARCHAR(100),
  presupuesto_min DECIMAL(12,2),
  presupuesto_max DECIMAL(12,2),
  moneda VARCHAR(10),
  fecha_cierre DATE,
  estado ENUM('activa','en_negociacion','cerrada','cancelada') DEFAULT 'activa',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_op_emp FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa) ON DELETE CASCADE,
  CONSTRAINT fk_op_camp FOREIGN KEY (id_campana) REFERENCES campanas(id_campana) ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE oportunidades_influencers (
  id_oportunidad_influencer INT AUTO_INCREMENT PRIMARY KEY,
  id_oportunidad INT NOT NULL,
  id_influencer INT NOT NULL,
  match_score DECIMAL(6,4),
  es_favorita TINYINT(1) DEFAULT 0,
  archivada_manualmente TINYINT(1) DEFAULT 0,
  estado_vista ENUM('nueva','vista') DEFAULT 'nueva',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY uq_oi (id_oportunidad,id_influencer),
  CONSTRAINT fk_oi_op FOREIGN KEY (id_oportunidad) REFERENCES oportunidades(id_oportunidad) ON DELETE CASCADE,
  CONSTRAINT fk_oi_inf FOREIGN KEY (id_influencer) REFERENCES influencers(id_influencer) ON DELETE CASCADE
) ENGINE=InnoDB;

-- =========================================================
-- PLANES / PAGOS / FACTURACIÓN
-- =========================================================
CREATE TABLE planes (
  id_plan INT AUTO_INCREMENT PRIMARY KEY,
  tipo_actor ENUM('empresa','influencer') NOT NULL,
  nombre_plan VARCHAR(100),
  descripcion TEXT,
  beneficios TEXT,
  limites TEXT,
  precio DECIMAL(12,2),
  prioridad INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE suscripciones (
  id_suscripcion INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT NOT NULL,
  id_plan INT NOT NULL,
  fecha_inicio DATE,
  fecha_vencimiento DATE,
  estado ENUM('activa','vencida','cancelada') DEFAULT 'activa',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_sus_user FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
  CONSTRAINT fk_sus_plan FOREIGN KEY (id_plan) REFERENCES planes(id_plan) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE pagos (
  id_pago INT AUTO_INCREMENT PRIMARY KEY,
  id_suscripcion INT,
  metodo ENUM('tarjeta','transferencia','pasarela') NOT NULL,
  monto_total DECIMAL(12,2),
  moneda VARCHAR(10),
  fecha_pago DATETIME,
  estado ENUM('pendiente','pagado','fallido') DEFAULT 'pendiente',
  comprobante_url VARCHAR(500),
  email_factura VARCHAR(250),
  rut_razon_social VARCHAR(100),
  direccion_facturacion TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_pago_sus FOREIGN KEY (id_suscripcion) REFERENCES suscripciones(id_suscripcion) ON DELETE SET NULL
) ENGINE=InnoDB;

-- =========================================================
-- NOTIFICACIONES
-- =========================================================
CREATE TABLE notificaciones (
  id_notificacion INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT NOT NULL,
  tipo ENUM('propuesta','contraoferta','servicio','campana','pago') NOT NULL,
  titulo VARCHAR(200),
  mensaje TEXT,
  --('normal','urgente')--
  urgencia VARCHAR(20),
  leida TINYINT(1) DEFAULT 0,
  url_redireccion VARCHAR(500),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_notif_user FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE preferencias_notificaciones (
  id_preferencia INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT NOT NULL,
  email_enabled TINYINT(1) DEFAULT 1,
  push_enabled TINYINT(1) DEFAULT 1,
  in_app_enabled TINYINT(1) DEFAULT 1,
  CONSTRAINT fk_pref_user FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
) ENGINE=InnoDB;
