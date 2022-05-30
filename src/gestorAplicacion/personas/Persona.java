package gestorAplicacion.personas;

import java.time.LocalDate;

import gestorAplicacion.general.Inventario;
import gestorAplicacion.ventas.Servicio;

import java.io.Serializable;

public class Persona implements Serializable {
	private static final long serialVersionUID = 1L;

	protected String nombre;
	protected String telefono;
	protected String email;
	protected String identificacion;
	protected TipoDocumento tipoDeIdentificacion;
	protected Sexo sexo;

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

	public void contratar(Persona personaElegida, String cargo, Servicio servicio, int salario, LocalDate fechaInicio,
			LocalDate fechaFin) {

	}

	public String mostrarInformacion() {
		return "Soy " + nombre + " con numero de indentificacion: " + identificacion;
	}

}
