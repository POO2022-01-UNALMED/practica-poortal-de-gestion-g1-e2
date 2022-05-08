package gestorAplicacion;

public class Persona {
	private String nombre;
	private String telefono;
	private String email;
	private String identificacion;
	private TipoDocumento tipoDeIdentificacion;
	private Sexo sexo;

	public Persona(String nombre, String telefono, String email, String identificacion,
			TipoDocumento tipoDeIdentificacion, Sexo sexo) {
		super();
		this.nombre = nombre;
		this.telefono = telefono;
		this.email = email;
		this.identificacion = identificacion;
		this.tipoDeIdentificacion = tipoDeIdentificacion;
		this.sexo = sexo;
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

}
