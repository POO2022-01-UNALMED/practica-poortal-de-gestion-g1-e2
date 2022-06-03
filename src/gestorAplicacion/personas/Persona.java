package gestorAplicacion.personas;

import java.time.LocalDate;
import java.util.ArrayList;

import gestorAplicacion.general.DiaSemana;
import gestorAplicacion.general.Inventario;
import gestorAplicacion.ventas.Servicio;

import java.io.Serializable;

/*
 * Esta clase funciona como la clase padre para las clases cliente y empleado, por tanto maneja los atributos basicos de una persona
 * 
 * @author Mateo Alvarez Lebrum
 * @author Alejandro Alvarez Botero
 * @author Miguel Angel Barrera Bustamante
 * @author Alejandra Barrientos Grisales
 *
 */
public class Persona implements Serializable {
	private static final long serialVersionUID = 1L;

	protected String nombre;
	protected String telefono;
	protected String email;
	protected String identificacion;
	protected TipoDocumento tipoDeIdentificacion;
	protected Sexo sexo;

	/**
	 * @param nombre
	 * @param telefono
	 * @param email
	 * @param identificacion
	 * @param tipoDeIdentificacion
	 * @param sexo
	 */
	public Persona(String nombre, String telefono, String email, String identificacion,
			TipoDocumento tipoDeIdentificacion, Sexo sexo) {
		super();
		this.nombre = nombre;
		this.telefono = telefono;
		this.email = email;
		this.identificacion = identificacion;
		this.tipoDeIdentificacion = tipoDeIdentificacion;
		this.sexo = sexo;
		Inventario.agregarPersona(this);
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getTelefono() {
		return telefono;
	}

	public void setTelefono(String telefono) {
		this.telefono = telefono;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getIdentificacion() {
		return identificacion;
	}

	public void setIdentificacion(String identificacion) {
		this.identificacion = identificacion;
	}

	public TipoDocumento getTipoDeIdentificacion() {
		return tipoDeIdentificacion;
	}

	public void setTipoDeIdentificacion(TipoDocumento tipoDeIdentificacion) {
		this.tipoDeIdentificacion = tipoDeIdentificacion;
	}

	public Sexo getSexo() {
		return sexo;
	}

	public void setSexo(Sexo sexo) {
		this.sexo = sexo;
	}

	/**
	 * @param contrato
	 * @param cargo
	 * @param servicio
	 * @param diasLaborales
	 * 
	 * @return crea una instancia de empleado
	 */
	public void contratar(Contrato contrato, String cargo, Servicio servicio, ArrayList<DiaSemana> diasLaborales) {
		new Empleado(this, contrato, cargo, servicio, diasLaborales);
	}

	/**
	 * @return String con la informacion de la persona
	 */
	public String mostrarInformacion() {
		return "Soy " + nombre + " con numero de indentificacion: " + identificacion;
	}

}
