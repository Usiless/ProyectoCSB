-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-04-2023 a las 05:02:36
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `csb_prov`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `afecciones`
--

CREATE TABLE `afecciones` (
  `idafeccion` int(11) NOT NULL,
  `descrpcion` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `idalumno` int(11) NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `documento` varchar(45) NOT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `idgrado` int(11) NOT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `user_id_user` int(11) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistencias`
--

CREATE TABLE `asistencias` (
  `idasistencia` int(11) NOT NULL,
  `idfecha` date NOT NULL DEFAULT current_timestamp(),
  `idhorario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auditoria`
--

CREATE TABLE `auditoria` (
  `idauditoria` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `fecha` datetime DEFAULT current_timestamp(),
  `tabla` varchar(45) NOT NULL,
  `tipo_cambio` varchar(45) NOT NULL,
  `datos_anteriores` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `doctores`
--

CREATE TABLE `doctores` (
  `iddoctor` int(11) NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `reg_prof` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fichas_medicas`
--

CREATE TABLE `fichas_medicas` (
  `idficha_medica` int(11) NOT NULL,
  `fecha` date NOT NULL DEFAULT current_timestamp(),
  `aptitud` char(1) NOT NULL DEFAULT 'A',
  `iddoctor` int(11) NOT NULL,
  `idalumno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grados`
--

CREATE TABLE `grados` (
  `idgrado` int(11) NOT NULL,
  `grado` varchar(45) NOT NULL,
  `idseccion` int(11) NOT NULL,
  `idnivel_escolar` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gravedad`
--

CREATE TABLE `gravedad` (
  `idgravedad` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_de_ingresos`
--

CREATE TABLE `historial_de_ingresos` (
  `idhistorial_de_ingreso` int(11) NOT NULL,
  `fecha` date NOT NULL DEFAULT current_timestamp(),
  `descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_observaciones`
--

CREATE TABLE `historial_observaciones` (
  `idhistorial_observaciones` int(11) NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `fecha` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horario`
--

CREATE TABLE `horario` (
  `idhorario` int(11) NOT NULL,
  `dia` set('1','2','3','4','5') NOT NULL,
  `idgrado` int(11) NOT NULL,
  `idmateria` int(11) NOT NULL,
  `idprofesor` int(11) NOT NULL,
  `inicio` time NOT NULL,
  `fin` time NOT NULL,
  `turno` tinyint(1) NOT NULL DEFAULT 1,
  `año` year(4) NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `indicadores`
--

CREATE TABLE `indicadores` (
  `idindicadores` int(11) NOT NULL,
  `descripción` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `indicadores_proceso`
--

CREATE TABLE `indicadores_proceso` (
  `idproceso` int(11) NOT NULL,
  `idindicadores` int(11) NOT NULL,
  `idalumno` int(11) NOT NULL,
  `logrado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `legajo`
--

CREATE TABLE `legajo` (
  `idlegajo` int(11) NOT NULL,
  `historial_académico` longblob DEFAULT NULL,
  `idprofesor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `idmateria` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias_de_grado`
--

CREATE TABLE `materias_de_grado` (
  `idgrado` int(11) NOT NULL,
  `idmateria` int(11) NOT NULL,
  `idprofesor` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nivel_escolar`
--

CREATE TABLE `nivel_escolar` (
  `idnivel_escolar` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `exigencia` int(11) NOT NULL,
  `horario_recreo_manhana` time DEFAULT NULL,
  `horario_recreo_tarde` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `noticias`
--

CREATE TABLE `noticias` (
  `idnoticias` int(11) NOT NULL,
  `fecha` date NOT NULL DEFAULT current_timestamp(),
  `titulo` varchar(45) DEFAULT NULL,
  `encabezado` varchar(250) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `autor` varchar(45) DEFAULT NULL,
  `user_id_user` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `observaciones`
--

CREATE TABLE `observaciones` (
  `idafeccion` int(11) NOT NULL,
  `idficha_medica` int(11) NOT NULL,
  `recomendacion` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `participantes`
--

CREATE TABLE `participantes` (
  `idhistorial_observaciones` int(11) NOT NULL,
  `idalumno` int(11) NOT NULL,
  `idgravedad` int(11) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permisos`
--

CREATE TABLE `permisos` (
  `idtipo_user` int(11) NOT NULL,
  `idtabla` int(11) NOT NULL,
  `crear` tinyint(4) NOT NULL DEFAULT 0,
  `leer` tinyint(4) NOT NULL DEFAULT 0,
  `actualizar` tinyint(4) NOT NULL DEFAULT 0,
  `borrar` tinyint(4) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `permisos`
--

INSERT INTO `permisos` (`idtipo_user`, `idtabla`, `crear`, `leer`, `actualizar`, `borrar`) VALUES
(1, 1, 1, 1, 1, 1),
(1, 2, 1, 1, 1, 1),
(1, 3, 1, 1, 1, 1),
(1, 4, 1, 1, 1, 1),
(1, 5, 1, 1, 1, 1),
(1, 6, 1, 1, 1, 1),
(1, 7, 1, 1, 1, 1),
(1, 8, 1, 1, 1, 1),
(1, 9, 1, 1, 1, 1),
(1, 10, 1, 1, 1, 1),
(1, 11, 1, 1, 1, 1),
(1, 12, 1, 1, 1, 1),
(1, 13, 1, 1, 1, 1),
(1, 14, 1, 1, 1, 1),
(1, 15, 1, 1, 1, 1),
(1, 16, 1, 1, 1, 1),
(1, 17, 1, 1, 1, 1),
(1, 18, 1, 1, 1, 1),
(1, 19, 1, 1, 1, 1),
(1, 20, 1, 1, 1, 1),
(1, 21, 1, 1, 1, 1),
(1, 22, 1, 1, 1, 1),
(1, 23, 1, 1, 1, 1),
(1, 24, 1, 1, 1, 1),
(1, 25, 1, 1, 1, 1),
(1, 26, 1, 1, 1, 1),
(1, 27, 1, 1, 1, 1),
(1, 28, 1, 1, 1, 1),
(1, 29, 1, 1, 1, 1),
(1, 30, 1, 1, 1, 1),
(1, 31, 1, 1, 1, 1),
(1, 32, 1, 1, 1, 1),
(1, 33, 1, 1, 1, 1),
(1, 34, 1, 1, 1, 1),
(1, 35, 1, 1, 1, 1),
(1, 37, 1, 1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal`
--

CREATE TABLE `personal` (
  `idpersonal` int(11) NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `documento` varchar(45) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `user_id_user` int(11) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plan_diario`
--

CREATE TABLE `plan_diario` (
  `idplan_diario` int(11) NOT NULL,
  `idgrado` int(11) NOT NULL,
  `idmateria` int(11) NOT NULL,
  `idprofesor` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `fecha` date NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `anexo` longblob DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presencias`
--

CREATE TABLE `presencias` (
  `idalumno` int(11) NOT NULL,
  `idasistencia` int(11) NOT NULL,
  `asistencia` tinyint(4) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `procesos`
--

CREATE TABLE `procesos` (
  `idproceso` int(11) NOT NULL,
  `idgrado` int(11) NOT NULL,
  `idmateria` int(11) NOT NULL,
  `idprofesor` int(11) NOT NULL,
  `titulo` varchar(45) NOT NULL,
  `total_puntos` int(11) NOT NULL,
  `fecha` date NOT NULL DEFAULT current_timestamp(),
  `fecha_entrega` date DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1,
  `idtipo_proceso` int(11) NOT NULL,
  `etapa` tinyint(1) NOT NULL,
  `capacidad` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE `profesores` (
  `idprofesor` int(11) NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `documento` varchar(45) NOT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `domicilio` varchar(45) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1,
  `user_id_user` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `relacion`
--

CREATE TABLE `relacion` (
  `idtutor` int(11) NOT NULL,
  `idalumno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `secciones`
--

CREATE TABLE `secciones` (
  `idseccion` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tablas`
--

CREATE TABLE `tablas` (
  `idtabla` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tablas`
--

INSERT INTO `tablas` (`idtabla`, `nombre`) VALUES
(1, 'afecciones'),
(2, 'alumnos'),
(3, 'asistencias'),
(4, 'auditoria'),
(5, 'doctores'),
(6, 'estado_procesos'),
(7, 'fichas_medicas'),
(8, 'grados'),
(9, 'gravedad'),
(10, 'historial_de_ingresos'),
(11, 'historial_observaciones'),
(12, 'horario'),
(13, 'indicadores'),
(14, 'indicadores_proceso'),
(15, 'legajo'),
(16, 'materias'),
(17, 'materias_de_grado'),
(18, 'nivel_escolar'),
(19, 'noticias'),
(20, 'observaciones'),
(21, 'permisos'),
(22, 'personal'),
(23, 'plan_diario'),
(24, 'presencias'),
(25, 'procesos'),
(26, 'profesores'),
(27, 'relacion'),
(28, 'secciones'),
(29, 'tablas'),
(30, 'tipo_procesos'),
(31, 'tipo_user'),
(32, 'tutores'),
(33, 'users'),
(34, 'visitantes'),
(35, 'visitantes_por_dia'),
(37, 'participantes');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_procesos`
--

CREATE TABLE `tipo_procesos` (
  `idtipo_proceso` int(11) NOT NULL,
  `descripcion` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_user`
--

CREATE TABLE `tipo_user` (
  `idtipo_user` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tipo_user`
--

INSERT INTO `tipo_user` (`idtipo_user`, `nombre`, `descripcion`) VALUES
(1, 'admin', ''),
(2, 'directivo', ''),
(3, 'profesor', ''),
(4, 'portero', ''),
(5, 'personal', ''),
(6, 'alumno', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tutores`
--

CREATE TABLE `tutores` (
  `idtutor` int(11) NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `documento` varchar(45) NOT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `domicilio` varchar(45) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id_user` int(11) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `username` varchar(16) DEFAULT NULL,
  `fullname` varchar(32) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL,
  `idtipo_user` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id_user`, `email`, `username`, `fullname`, `password`, `idtipo_user`, `estado`) VALUES
(1, 'a', 'admin', 'admin', 'pbkdf2:sha256:260000$gLDoV5zaY3DV0cja$37c0cb06baac20cb9da6b654cf68f298c704627c7eedec55369e6f2cbbbc2340', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visitantes`
--

CREATE TABLE `visitantes` (
  `idvisitante` int(11) NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visitantes_por_dia`
--

CREATE TABLE `visitantes_por_dia` (
  `idhistorial_de_ingreso` int(11) NOT NULL,
  `idvisitante` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `afecciones`
--
ALTER TABLE `afecciones`
  ADD PRIMARY KEY (`idafeccion`);

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`idalumno`),
  ADD KEY `fk_alumnos_grado1` (`idgrado`),
  ADD KEY `fk_alumnos_user1` (`user_id_user`);

--
-- Indices de la tabla `asistencias`
--
ALTER TABLE `asistencias`
  ADD PRIMARY KEY (`idasistencia`),
  ADD KEY `fk_asistencias_horario1` (`idhorario`);

--
-- Indices de la tabla `auditoria`
--
ALTER TABLE `auditoria`
  ADD PRIMARY KEY (`idauditoria`),
  ADD KEY `fk_auditoria_user1` (`id_user`);

--
-- Indices de la tabla `doctores`
--
ALTER TABLE `doctores`
  ADD PRIMARY KEY (`iddoctor`);

--
-- Indices de la tabla `fichas_medicas`
--
ALTER TABLE `fichas_medicas`
  ADD PRIMARY KEY (`idficha_medica`),
  ADD KEY `fk_ficha_medica_alumnos1` (`idalumno`),
  ADD KEY `fk_fichas_medicas_doctores1` (`iddoctor`);

--
-- Indices de la tabla `grados`
--
ALTER TABLE `grados`
  ADD PRIMARY KEY (`idgrado`),
  ADD KEY `fk_grados_secciones1` (`idseccion`),
  ADD KEY `fk_grados_nivel_escolar1` (`idnivel_escolar`);

--
-- Indices de la tabla `gravedad`
--
ALTER TABLE `gravedad`
  ADD PRIMARY KEY (`idgravedad`);

--
-- Indices de la tabla `historial_de_ingresos`
--
ALTER TABLE `historial_de_ingresos`
  ADD PRIMARY KEY (`idhistorial_de_ingreso`);

--
-- Indices de la tabla `historial_observaciones`
--
ALTER TABLE `historial_observaciones`
  ADD PRIMARY KEY (`idhistorial_observaciones`);

--
-- Indices de la tabla `horario`
--
ALTER TABLE `horario`
  ADD PRIMARY KEY (`idhorario`),
  ADD KEY `fk_horario_materias_de_grado1` (`idgrado`,`idmateria`,`idprofesor`);

--
-- Indices de la tabla `indicadores`
--
ALTER TABLE `indicadores`
  ADD PRIMARY KEY (`idindicadores`);

--
-- Indices de la tabla `indicadores_proceso`
--
ALTER TABLE `indicadores_proceso`
  ADD PRIMARY KEY (`idproceso`,`idindicadores`,`idalumno`),
  ADD KEY `fk_procesos_has_indicadores_indicadores1` (`idindicadores`),
  ADD KEY `fk_indicadores_proceso_alumnos1` (`idalumno`);

--
-- Indices de la tabla `legajo`
--
ALTER TABLE `legajo`
  ADD PRIMARY KEY (`idlegajo`),
  ADD KEY `fk_legajo_profesores1` (`idprofesor`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`idmateria`);

--
-- Indices de la tabla `materias_de_grado`
--
ALTER TABLE `materias_de_grado`
  ADD PRIMARY KEY (`idgrado`,`idmateria`,`idprofesor`),
  ADD KEY `fk_materias_de_grado_materias1` (`idmateria`),
  ADD KEY `fk_materias_de_grado_profesores1` (`idprofesor`);

--
-- Indices de la tabla `nivel_escolar`
--
ALTER TABLE `nivel_escolar`
  ADD PRIMARY KEY (`idnivel_escolar`);

--
-- Indices de la tabla `noticias`
--
ALTER TABLE `noticias`
  ADD PRIMARY KEY (`idnoticias`),
  ADD KEY `fk_noticias_user1` (`user_id_user`);

--
-- Indices de la tabla `observaciones`
--
ALTER TABLE `observaciones`
  ADD PRIMARY KEY (`idafeccion`,`idficha_medica`),
  ADD KEY `fk_afecciones_has_fichas_medicas_fichas_medicas1` (`idficha_medica`);

--
-- Indices de la tabla `participantes`
--
ALTER TABLE `participantes`
  ADD PRIMARY KEY (`idhistorial_observaciones`,`idalumno`),
  ADD KEY `fk_historial_observaciones_has_alumnos_alumnos1` (`idalumno`),
  ADD KEY `fk_historial_observaciones_has_alumnos_gravedad1` (`idgravedad`);

--
-- Indices de la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`idtipo_user`,`idtabla`),
  ADD KEY `fk_tipo_user_has_tablas_tablas1` (`idtabla`);

--
-- Indices de la tabla `personal`
--
ALTER TABLE `personal`
  ADD PRIMARY KEY (`idpersonal`),
  ADD KEY `fk_personal_user1` (`user_id_user`);

--
-- Indices de la tabla `plan_diario`
--
ALTER TABLE `plan_diario`
  ADD PRIMARY KEY (`idplan_diario`),
  ADD KEY `fk_plan_diario_materias_de_grado1` (`idgrado`,`idmateria`,`idprofesor`);

--
-- Indices de la tabla `presencias`
--
ALTER TABLE `presencias`
  ADD PRIMARY KEY (`idalumno`,`idasistencia`),
  ADD KEY `fk_alumnos_has_asistencias_asistencias1` (`idasistencia`);

--
-- Indices de la tabla `procesos`
--
ALTER TABLE `procesos`
  ADD PRIMARY KEY (`idproceso`),
  ADD KEY `fk_procesos_tipo_procesos1` (`idtipo_proceso`),
  ADD KEY `fk_procesos_materias_de_grado1` (`idgrado`,`idmateria`,`idprofesor`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`idprofesor`),
  ADD KEY `fk_profesores_user1` (`user_id_user`);

--
-- Indices de la tabla `relacion`
--
ALTER TABLE `relacion`
  ADD PRIMARY KEY (`idtutor`,`idalumno`),
  ADD KEY `fk_tutores_has_alumnos_alumnos1` (`idalumno`);

--
-- Indices de la tabla `secciones`
--
ALTER TABLE `secciones`
  ADD PRIMARY KEY (`idseccion`);

--
-- Indices de la tabla `tablas`
--
ALTER TABLE `tablas`
  ADD PRIMARY KEY (`idtabla`);

--
-- Indices de la tabla `tipo_procesos`
--
ALTER TABLE `tipo_procesos`
  ADD PRIMARY KEY (`idtipo_proceso`);

--
-- Indices de la tabla `tipo_user`
--
ALTER TABLE `tipo_user`
  ADD PRIMARY KEY (`idtipo_user`);

--
-- Indices de la tabla `tutores`
--
ALTER TABLE `tutores`
  ADD PRIMARY KEY (`idtutor`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`),
  ADD KEY `fk_user_tipo_user1` (`idtipo_user`);

--
-- Indices de la tabla `visitantes`
--
ALTER TABLE `visitantes`
  ADD PRIMARY KEY (`idvisitante`);

--
-- Indices de la tabla `visitantes_por_dia`
--
ALTER TABLE `visitantes_por_dia`
  ADD PRIMARY KEY (`idhistorial_de_ingreso`,`idvisitante`),
  ADD KEY `fk_historial_de_ingresos_has_visitantes_visitantes1` (`idvisitante`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `afecciones`
--
ALTER TABLE `afecciones`
  MODIFY `idafeccion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `idalumno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `asistencias`
--
ALTER TABLE `asistencias`
  MODIFY `idasistencia` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auditoria`
--
ALTER TABLE `auditoria`
  MODIFY `idauditoria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `doctores`
--
ALTER TABLE `doctores`
  MODIFY `iddoctor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fichas_medicas`
--
ALTER TABLE `fichas_medicas`
  MODIFY `idficha_medica` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `grados`
--
ALTER TABLE `grados`
  MODIFY `idgrado` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `gravedad`
--
ALTER TABLE `gravedad`
  MODIFY `idgravedad` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `historial_de_ingresos`
--
ALTER TABLE `historial_de_ingresos`
  MODIFY `idhistorial_de_ingreso` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `historial_observaciones`
--
ALTER TABLE `historial_observaciones`
  MODIFY `idhistorial_observaciones` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `horario`
--
ALTER TABLE `horario`
  MODIFY `idhorario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `indicadores`
--
ALTER TABLE `indicadores`
  MODIFY `idindicadores` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `legajo`
--
ALTER TABLE `legajo`
  MODIFY `idlegajo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `materias`
--
ALTER TABLE `materias`
  MODIFY `idmateria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `nivel_escolar`
--
ALTER TABLE `nivel_escolar`
  MODIFY `idnivel_escolar` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `noticias`
--
ALTER TABLE `noticias`
  MODIFY `idnoticias` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `personal`
--
ALTER TABLE `personal`
  MODIFY `idpersonal` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `plan_diario`
--
ALTER TABLE `plan_diario`
  MODIFY `idplan_diario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `procesos`
--
ALTER TABLE `procesos`
  MODIFY `idproceso` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `profesores`
--
ALTER TABLE `profesores`
  MODIFY `idprofesor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `secciones`
--
ALTER TABLE `secciones`
  MODIFY `idseccion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tablas`
--
ALTER TABLE `tablas`
  MODIFY `idtabla` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `tipo_procesos`
--
ALTER TABLE `tipo_procesos`
  MODIFY `idtipo_proceso` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_user`
--
ALTER TABLE `tipo_user`
  MODIFY `idtipo_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `tutores`
--
ALTER TABLE `tutores`
  MODIFY `idtutor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `visitantes`
--
ALTER TABLE `visitantes`
  MODIFY `idvisitante` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD CONSTRAINT `fk_alumnos_grado1` FOREIGN KEY (`idgrado`) REFERENCES `grados` (`idgrado`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_alumnos_user1` FOREIGN KEY (`user_id_user`) REFERENCES `users` (`id_user`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `asistencias`
--
ALTER TABLE `asistencias`
  ADD CONSTRAINT `fk_asistencias_horario1` FOREIGN KEY (`idhorario`) REFERENCES `horario` (`idhorario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `auditoria`
--
ALTER TABLE `auditoria`
  ADD CONSTRAINT `fk_auditoria_user1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `fichas_medicas`
--
ALTER TABLE `fichas_medicas`
  ADD CONSTRAINT `fk_ficha_medica_alumnos1` FOREIGN KEY (`idalumno`) REFERENCES `alumnos` (`idalumno`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_fichas_medicas_doctores1` FOREIGN KEY (`iddoctor`) REFERENCES `doctores` (`iddoctor`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `grados`
--
ALTER TABLE `grados`
  ADD CONSTRAINT `fk_grados_nivel_escolar1` FOREIGN KEY (`idnivel_escolar`) REFERENCES `nivel_escolar` (`idnivel_escolar`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_grados_secciones1` FOREIGN KEY (`idseccion`) REFERENCES `secciones` (`idseccion`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `horario`
--
ALTER TABLE `horario`
  ADD CONSTRAINT `fk_horario_materias_de_grado1` FOREIGN KEY (`idgrado`,`idmateria`,`idprofesor`) REFERENCES `materias_de_grado` (`idgrado`, `idmateria`, `idprofesor`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `indicadores_proceso`
--
ALTER TABLE `indicadores_proceso`
  ADD CONSTRAINT `fk_indicadores_proceso_alumnos1` FOREIGN KEY (`idalumno`) REFERENCES `alumnos` (`idalumno`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_procesos_has_indicadores_indicadores1` FOREIGN KEY (`idindicadores`) REFERENCES `indicadores` (`idindicadores`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_procesos_has_indicadores_procesos1` FOREIGN KEY (`idproceso`) REFERENCES `procesos` (`idproceso`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `legajo`
--
ALTER TABLE `legajo`
  ADD CONSTRAINT `fk_legajo_profesores1` FOREIGN KEY (`idprofesor`) REFERENCES `profesores` (`idprofesor`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `materias_de_grado`
--
ALTER TABLE `materias_de_grado`
  ADD CONSTRAINT `fk_grado_has_pofesores_de_materias_grado1` FOREIGN KEY (`idgrado`) REFERENCES `grados` (`idgrado`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_materias_de_grado_materias1` FOREIGN KEY (`idmateria`) REFERENCES `materias` (`idmateria`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_materias_de_grado_profesores1` FOREIGN KEY (`idprofesor`) REFERENCES `profesores` (`idprofesor`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `noticias`
--
ALTER TABLE `noticias`
  ADD CONSTRAINT `fk_noticias_user1` FOREIGN KEY (`user_id_user`) REFERENCES `users` (`id_user`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `observaciones`
--
ALTER TABLE `observaciones`
  ADD CONSTRAINT `fk_afecciones_has_fichas_medicas_afecciones1` FOREIGN KEY (`idafeccion`) REFERENCES `afecciones` (`idafeccion`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_afecciones_has_fichas_medicas_fichas_medicas1` FOREIGN KEY (`idficha_medica`) REFERENCES `fichas_medicas` (`idficha_medica`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `participantes`
--
ALTER TABLE `participantes`
  ADD CONSTRAINT `fk_historial_observaciones_has_alumnos_alumnos1` FOREIGN KEY (`idalumno`) REFERENCES `alumnos` (`idalumno`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_historial_observaciones_has_alumnos_gravedad1` FOREIGN KEY (`idgravedad`) REFERENCES `gravedad` (`idgravedad`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_historial_observaciones_has_alumnos_historial_observaciones1` FOREIGN KEY (`idhistorial_observaciones`) REFERENCES `historial_observaciones` (`idhistorial_observaciones`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD CONSTRAINT `fk_tipo_user_has_tablas_tablas1` FOREIGN KEY (`idtabla`) REFERENCES `tablas` (`idtabla`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_tipo_user_has_tablas_tipo_user1` FOREIGN KEY (`idtipo_user`) REFERENCES `tipo_user` (`idtipo_user`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `personal`
--
ALTER TABLE `personal`
  ADD CONSTRAINT `fk_personal_user1` FOREIGN KEY (`user_id_user`) REFERENCES `users` (`id_user`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `plan_diario`
--
ALTER TABLE `plan_diario`
  ADD CONSTRAINT `fk_plan_diario_materias_de_grado1` FOREIGN KEY (`idgrado`,`idmateria`,`idprofesor`) REFERENCES `materias_de_grado` (`idgrado`, `idmateria`, `idprofesor`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `presencias`
--
ALTER TABLE `presencias`
  ADD CONSTRAINT `fk_alumnos_has_asistencias_alumnos1` FOREIGN KEY (`idalumno`) REFERENCES `alumnos` (`idalumno`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_alumnos_has_asistencias_asistencias1` FOREIGN KEY (`idasistencia`) REFERENCES `asistencias` (`idasistencia`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `procesos`
--
ALTER TABLE `procesos`
  ADD CONSTRAINT `fk_procesos_materias_de_grado1` FOREIGN KEY (`idgrado`,`idmateria`,`idprofesor`) REFERENCES `materias_de_grado` (`idgrado`, `idmateria`, `idprofesor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_procesos_tipo_procesos1` FOREIGN KEY (`idtipo_proceso`) REFERENCES `tipo_procesos` (`idtipo_proceso`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD CONSTRAINT `fk_profesores_user1` FOREIGN KEY (`user_id_user`) REFERENCES `users` (`id_user`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `relacion`
--
ALTER TABLE `relacion`
  ADD CONSTRAINT `fk_tutores_has_alumnos_alumnos1` FOREIGN KEY (`idalumno`) REFERENCES `alumnos` (`idalumno`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_tutores_has_alumnos_tutores` FOREIGN KEY (`idtutor`) REFERENCES `tutores` (`idtutor`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fk_user_tipo_user1` FOREIGN KEY (`idtipo_user`) REFERENCES `tipo_user` (`idtipo_user`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `visitantes_por_dia`
--
ALTER TABLE `visitantes_por_dia`
  ADD CONSTRAINT `fk_historial_de_ingresos_has_visitantes_historial_de_ingresos1` FOREIGN KEY (`idhistorial_de_ingreso`) REFERENCES `historial_de_ingresos` (`idhistorial_de_ingreso`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_historial_de_ingresos_has_visitantes_visitantes1` FOREIGN KEY (`idvisitante`) REFERENCES `visitantes` (`idvisitante`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
