SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


CREATE SCHEMA IF NOT EXISTS `csb_prov` DEFAULT CHARACTER SET utf8 ;
USE `csb_prov` ;

-- -----------------------------------------------------
-- Table `csb_prov`.`tipo_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`tipo_user` (
  `idtipo_user` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripción` VARCHAR(45) NULL,
  PRIMARY KEY (`idtipo_user`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`users` (
  `id_user` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(16) NULL,
  `fullname` VARCHAR(32) NULL,
  `password` VARCHAR(100) NULL,
  `idtipo_user` INT NOT NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id_user`),
  CONSTRAINT `fk_user_tipo_user1`
    FOREIGN KEY (`idtipo_user`)
    REFERENCES `csb_prov`.`tipo_user` (`idtipo_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `csb_prov`.`secciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`secciones` (
  `idseccion` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idseccion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`nivel_escolar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`nivel_escolar` (
  `idnivel_escolar` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `exigencia` INT NOT NULL,
  PRIMARY KEY (`idnivel_escolar`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`grados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`grados` (
  `idgrado` INT NOT NULL AUTO_INCREMENT,
  `grado` VARCHAR(45) NOT NULL,
  `idseccion` INT NOT NULL,
  `idnivel_escolar` INT NOT NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`idgrado`),
  CONSTRAINT `fk_grados_secciones1`
    FOREIGN KEY (`idseccion`)
    REFERENCES `csb_prov`.`secciones` (`idseccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_grados_nivel_escolar1`
    FOREIGN KEY (`idnivel_escolar`)
    REFERENCES `csb_prov`.`nivel_escolar` (`idnivel_escolar`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`alumnos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`alumnos` (
  `idalumno` INT NOT NULL AUTO_INCREMENT,
  `nombres` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  `documento` VARCHAR(45) NOT NULL,
  `celular` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `idgrado` INT NOT NULL,
  `fecha_nacimiento` DATE NULL,
  `user_id_user` INT NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`idalumno`),
  CONSTRAINT `fk_alumnos_grado1`
    FOREIGN KEY (`idgrado`)
    REFERENCES `csb_prov`.`grados` (`idgrado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_alumnos_user1`
    FOREIGN KEY (`user_id_user`)
    REFERENCES `csb_prov`.`users` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`profesores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`profesores` (
  `idprofesor` INT NOT NULL AUTO_INCREMENT,
  `nombres` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  `documento` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NULL,
  `celular` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `domicilio` VARCHAR(45) NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 1,
  `user_id_user` INT NULL,
  PRIMARY KEY (`idprofesor`),
  CONSTRAINT `fk_profesores_user1`
    FOREIGN KEY (`user_id_user`)
    REFERENCES `csb_prov`.`users` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`personal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`personal` (
  `idpersonal` INT NOT NULL AUTO_INCREMENT,
  `nombres` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  `documento` VARCHAR(45) NOT NULL,
  `celular` VARCHAR(45) NULL,
  `user_id_user` INT NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`idpersonal`),
  CONSTRAINT `fk_personal_user1`
    FOREIGN KEY (`user_id_user`)
    REFERENCES `csb_prov`.`users` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`tutores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`tutores` (
  `idtutor` INT NOT NULL AUTO_INCREMENT,
  `nombres` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  `documento` VARCHAR(45) NOT NULL,
  `celular` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `domicilio` VARCHAR(45) NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`idtutor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`relacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`relacion` (
  `idtutor` INT NOT NULL,
  `idalumno` INT NOT NULL,
  PRIMARY KEY (`idtutor`, `idalumno`),
  CONSTRAINT `fk_tutores_has_alumnos_tutores`
    FOREIGN KEY (`idtutor`)
    REFERENCES `csb_prov`.`tutores` (`idtutor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tutores_has_alumnos_alumnos1`
    FOREIGN KEY (`idalumno`)
    REFERENCES `csb_prov`.`alumnos` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`materias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`materias` (
  `idmateria` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(250) NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`idmateria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`materias_de_grado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`materias_de_grado` (
  `idgrado` INT NOT NULL,
  `idmateria` INT NOT NULL,
  `idprofesor` INT NOT NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`idgrado`, `idmateria`, `idprofesor`),
  CONSTRAINT `fk_grado_has_pofesores_de_materias_grado1`
    FOREIGN KEY (`idgrado`)
    REFERENCES `csb_prov`.`grados` (`idgrado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_materias_de_grado_materias1`
    FOREIGN KEY (`idmateria`)
    REFERENCES `csb_prov`.`materias` (`idmateria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_materias_de_grado_profesores1`
    FOREIGN KEY (`idprofesor`)
    REFERENCES `csb_prov`.`profesores` (`idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`horario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`horario` (
  `idhorario` INT NOT NULL AUTO_INCREMENT,
  `dia` INT NOT NULL,
  `idgrado` INT NOT NULL,
  `idmateria` INT NOT NULL,
  `idprofesor` INT NOT NULL,
  `inicio` TIME NOT NULL,
  `fin` TIME NOT NULL,
  `turno` TINYINT(1) NOT NULL DEFAULT 1,
  `año` YEAR NOT NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`idhorario`),
  CONSTRAINT `fk_horario_materias_de_grado1`
    FOREIGN KEY (`idgrado` , `idmateria` , `idprofesor`)
    REFERENCES `csb_prov`.`materias_de_grado` (`idgrado` , `idmateria` , `idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`tipo_procesos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`tipo_procesos` (
  `idtipo_proceso` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtipo_proceso`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`procesos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`procesos` (
  `idproceso` INT NOT NULL AUTO_INCREMENT,
  `idgrado` INT NOT NULL,
  `idmateria` INT NOT NULL,
  `idprofesor` INT NOT NULL,
  `titulo` VARCHAR(45) NOT NULL,
  `total_puntos` INT NOT NULL,
  `fecha` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_entrega` DATE NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 0,
  `idtipo_proceso` INT NOT NULL,
  PRIMARY KEY (`idproceso`),
  CONSTRAINT `fk_procesos_tipo_procesos1`
    FOREIGN KEY (`idtipo_proceso`)
    REFERENCES `csb_prov`.`tipo_procesos` (`idtipo_proceso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_procesos_materias_de_grado1`
    FOREIGN KEY (`idgrado` , `idmateria` , `idprofesor`)
    REFERENCES `csb_prov`.`materias_de_grado` (`idgrado` , `idmateria` , `idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`indicadores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`indicadores` (
  `idindicadores` INT NOT NULL AUTO_INCREMENT,
  `descripción` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`idindicadores`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`estado_procesos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`estado_procesos` (
  `idalumno` INT NOT NULL,
  `idtarea` INT NOT NULL,
  `puntos_logrados` INT NOT NULL,
  PRIMARY KEY (`idalumno`, `idtarea`),
  CONSTRAINT `fk_alumnos_has_tareas_alumnos1`
    FOREIGN KEY (`idalumno`)
    REFERENCES `csb_prov`.`alumnos` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_alumnos_has_tareas_tareas1`
    FOREIGN KEY (`idtarea`)
    REFERENCES `csb_prov`.`procesos` (`idproceso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`asistencias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`asistencias` (
  `idasistencia` INT NOT NULL AUTO_INCREMENT,
  `idfecha` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `idhorario` INT NOT NULL,
  PRIMARY KEY (`idasistencia`),
  CONSTRAINT `fk_asistencias_horario1`
    FOREIGN KEY (`idhorario`)
    REFERENCES `csb_prov`.`horario` (`idhorario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`gravedad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`gravedad` (
  `idgravedad` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(250) NULL,
  PRIMARY KEY (`idgravedad`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`historial_observaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`historial_observaciones` (
  `idhistorial_observaciones` INT NOT NULL AUTO_INCREMENT,
  `idalumno` INT NOT NULL,
  `descripción` VARCHAR(45) NOT NULL,
  `fecha` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `gravedad_idgravedad` INT NOT NULL,
  PRIMARY KEY (`idhistorial_observaciones`),
  CONSTRAINT `fk_historial_observaciones_alumnos1`
    FOREIGN KEY (`idalumno`)
    REFERENCES `csb_prov`.`alumnos` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_historial_observaciones_gravedad1`
    FOREIGN KEY (`gravedad_idgravedad`)
    REFERENCES `csb_prov`.`gravedad` (`idgravedad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`visitantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`visitantes` (
  `idvisitante` INT NOT NULL AUTO_INCREMENT,
  `nombres` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`idvisitante`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`historial_de_ingresos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`historial_de_ingresos` (
  `idhistorial_de_ingreso` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`idhistorial_de_ingreso`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`indicadores_proceso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`indicadores_proceso` (
  `idproceso` INT NOT NULL,
  `idindicadores` INT NOT NULL,
  `alumnos_idalumno` INT NOT NULL,
  `logrado` TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`idproceso`, `idindicadores`, `alumnos_idalumno`),
  CONSTRAINT `fk_procesos_has_indicadores_procesos1`
    FOREIGN KEY (`idproceso`)
    REFERENCES `csb_prov`.`procesos` (`idproceso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_procesos_has_indicadores_indicadores1`
    FOREIGN KEY (`idindicadores`)
    REFERENCES `csb_prov`.`indicadores` (`idindicadores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_indicadores_proceso_alumnos1`
    FOREIGN KEY (`alumnos_idalumno`)
    REFERENCES `csb_prov`.`alumnos` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`visitantes_por_dia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`visitantes_por_dia` (
  `idhistorial_de_ingreso` INT NOT NULL,
  `idvisitante` INT NOT NULL,
  PRIMARY KEY (`idhistorial_de_ingreso`, `idvisitante`),
  CONSTRAINT `fk_historial_de_ingresos_has_visitantes_historial_de_ingresos1`
    FOREIGN KEY (`idhistorial_de_ingreso`)
    REFERENCES `csb_prov`.`historial_de_ingresos` (`idhistorial_de_ingreso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_historial_de_ingresos_has_visitantes_visitantes1`
    FOREIGN KEY (`idvisitante`)
    REFERENCES `csb_prov`.`visitantes` (`idvisitante`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`plan_diario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`plan_diario` (
  `idplan_diario` INT NOT NULL AUTO_INCREMENT,
  `idgrado` INT NOT NULL,
  `idmateria` INT NOT NULL,
  `idprofesor` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `fecha` DATE NOT NULL,
  `descripcion` VARCHAR(200) NULL,
  `anexo` BLOB NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`idplan_diario`),
  CONSTRAINT `fk_plan_diario_materias_de_grado1`
    FOREIGN KEY (`idgrado` , `idmateria` , `idprofesor`)
    REFERENCES `csb_prov`.`materias_de_grado` (`idgrado` , `idmateria` , `idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`auditoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`auditoria` (
  `idauditoria` INT NOT NULL AUTO_INCREMENT,
  `id_user` INT NOT NULL,
  `fecha` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `tabla` VARCHAR(45) NOT NULL,
  `tipo_cambio` VARCHAR(45) NOT NULL,
  `datos_anteriores` VARCHAR(500) NULL,
  PRIMARY KEY (`idauditoria`),
  CONSTRAINT `fk_auditoria_user1`
    FOREIGN KEY (`id_user`)
    REFERENCES `csb_prov`.`users` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`noticias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`noticias` (
  `idnoticias` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `tipo` VARCHAR(45) NULL,
  `descripción` VARCHAR(250) NULL,
  `autor` VARCHAR(45) NULL,
  `user_id_user` INT NOT NULL,
  PRIMARY KEY (`idnoticias`),
  CONSTRAINT `fk_noticias_user1`
    FOREIGN KEY (`user_id_user`)
    REFERENCES `csb_prov`.`users` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`legajo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`legajo` (
  `idlegajo` INT NOT NULL AUTO_INCREMENT,
  `historial_académico` LONGBLOB NULL,
  `idprofesor` INT NOT NULL,
  PRIMARY KEY (`idlegajo`),
  CONSTRAINT `fk_legajo_profesores1`
    FOREIGN KEY (`idprofesor`)
    REFERENCES `csb_prov`.`profesores` (`idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`tablas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`tablas` (
  `idtabla` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtabla`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`permisos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`permisos` (
  `idtipo_user` INT NOT NULL,
  `idtabla` INT NOT NULL,
  `crear` TINYINT NOT NULL DEFAULT 0,
  `leer` TINYINT NOT NULL DEFAULT 0,
  `actualizar` TINYINT NOT NULL DEFAULT 0,
  `borrar` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`idtipo_user`, `idtabla`),
  CONSTRAINT `fk_tipo_user_has_tablas_tipo_user1`
    FOREIGN KEY (`idtipo_user`)
    REFERENCES `csb_prov`.`tipo_user` (`idtipo_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tipo_user_has_tablas_tablas1`
    FOREIGN KEY (`idtabla`)
    REFERENCES `csb_prov`.`tablas` (`idtabla`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`doctores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`doctores` (
  `iddoctor` INT NOT NULL,
  `nombres` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  `reg_prof` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`iddoctor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`fichas_medicas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`fichas_medicas` (
  `idficha_medica` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `aptitud` TINYINT(1) NOT NULL DEFAULT 1,
  `iddoctor` INT NOT NULL,
  `idalumno` INT NOT NULL,
  PRIMARY KEY (`idficha_medica`),
  CONSTRAINT `fk_ficha_medica_alumnos1`
    FOREIGN KEY (`idalumno`)
    REFERENCES `csb_prov`.`alumnos` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fichas_medicas_doctores1`
    FOREIGN KEY (`iddoctor`)
    REFERENCES `csb_prov`.`doctores` (`iddoctor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`afecciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`afecciones` (
  `idafeccion` INT NOT NULL AUTO_INCREMENT,
  `descrpcion` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`idafeccion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`observaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`observaciones` (
  `idafeccion` INT NOT NULL,
  `idficha_medica` INT NOT NULL,
  `recomendacion` VARCHAR(250) NULL,
  PRIMARY KEY (`idafeccion`, `idficha_medica`),
  CONSTRAINT `fk_afecciones_has_fichas_medicas_afecciones1`
    FOREIGN KEY (`idafeccion`)
    REFERENCES `csb_prov`.`afecciones` (`idafeccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_afecciones_has_fichas_medicas_fichas_medicas1`
    FOREIGN KEY (`idficha_medica`)
    REFERENCES `csb_prov`.`fichas_medicas` (`idficha_medica`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `csb_prov`.`presencias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `csb_prov`.`presencias` (
  `idalumno` INT NOT NULL,
  `idasistencia` INT NOT NULL,
  `asistencia` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`idalumno`, `idasistencia`),
  CONSTRAINT `fk_alumnos_has_asistencias_alumnos1`
    FOREIGN KEY (`idalumno`)
    REFERENCES `csb_prov`.`alumnos` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_alumnos_has_asistencias_asistencias1`
    FOREIGN KEY (`idasistencia`)
    REFERENCES `csb_prov`.`asistencias` (`idasistencia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
