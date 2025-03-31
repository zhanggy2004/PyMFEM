namespace mfem {
  // serial
%pythonappend ComplexLinearForm::AddDomainIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(args[0], "thisown"):
        args[0].thisown = 0
        self._integrators.append(args[0])
    if hasattr(args[1], "thisown"):
        args[1].thisown = 0
        self._integrators.append(args[1])
%}
%pythonappend ComplexLinearForm::AddBoundaryIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(args[0], "thisown"):
        args[0].thisown = 0
        self._integrators.append(args[0])
    if hasattr(args[1], "thisown"):
        args[1].thisown = 0
        self._integrators.append(args[1])
%}
%pythonappend ComplexLinearForm::AddBdrFaceIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(args[0], "thisown"):
        args[0].thisown = 0
        self._integrators.append(args[0])
    if hasattr(args[1], "thisown"):
        args[1].thisown = 0
        self._integrators.append(args[1])
%}
%pythonappend SesquilinearForm::AddDomainIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(args[0], "thisown"):
        args[0].thisown = 0
        self._integrators.append(args[0])
    if hasattr(args[1], "thisown"):
        args[1].thisown = 0
        self._integrators.append(args[1])
%}
%pythonappend SesquilinearForm::AddBoundaryIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(args[0], "thisown"):
        args[0].thisown = 0
        self._integrators.append(args[0])
    if hasattr(args[1], "thisown"):
        args[1].thisown = 0
        self._integrators.append(args[1])
%}
%pythonappend SesquilinearForm::AddInteriorFaceIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(bfi_real, "thisown"):
        bfi_real.thisown = 0
        self._integrators.append(bfi_real)
    if hasattr(bfi_imag, "thisown"):
        bfi_imag.thisown = 0
        self._integrators.append(bfi_imag)
%}
%pythonappend SesquilinearForm::AddBdrFaceIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(args[0], "thisown"):
        args[0].thisown = 0
        self._integrators.append(args[0])
    if hasattr(args[1], "thisown"):
        args[1].thisown = 0
        self._integrators.append(args[1])
%}
  // parallel
%pythonappend ParComplexLinearForm::AddDomainIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(args[0], "thisown"):
        args[0].thisown = 0
        self._integrators.append(args[0])
    if hasattr(args[1], "thisown"):
        args[1].thisown = 0
        self._integrators.append(args[1])
%}
%pythonappend ParComplexLinearForm::AddBoundaryIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(args[0], "thisown"):
        args[0].thisown = 0
        self._integrators.append(args[0])
    if hasattr(args[1], "thisown"):
        args[1].thisown = 0
        self._integrators.append(args[1])
%}
%pythonappend ParComplexLinearForm::AddBdrFaceIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(args[0], "thisown"):
        args[0].thisown = 0
        self._integrators.append(args[0])
    if hasattr(args[1], "thisown"):
        args[1].thisown = 0
        self._integrators.append(args[1])
%}
%pythonappend ParSesquilinearForm::AddDomainIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(args[0], "thisown"):
        args[0].thisown = 0
        self._integrators.append(args[0])
    if hasattr(args[1], "thisown"):
        args[1].thisown = 0
        self._integrators.append(args[1])
%}
%pythonappend ParSesquilinearForm::AddBoundaryIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(args[0], "thisown"):
        args[0].thisown = 0
        self._integrators.append(args[0])
    if hasattr(args[1], "thisown"):
        args[1].thisown = 0
        self._integrators.append(args[1])
%}
%pythonappend ParSesquilinearForm::AddInteriorFaceIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(bfi_real, "thisown"):
        bfi_real.thisown = 0
        self._integrators.append(bfi_real)
    if hasattr(bfi_imag, "thisown"):
        bfi_imag.thisown = 0
        self._integrators.append(bfi_imag)
%}
%pythonappend ParSesquilinearForm::AddBdrFaceIntegrator %{
    if not hasattr(self, "_integrators"):
        self._integrators = []
    if hasattr(args[0], "thisown"):
        args[0].thisown = 0
        self._integrators.append(args[0])
    if hasattr(args[1], "thisown"):
        args[1].thisown = 0
        self._integrators.append(args[1])
%}

}
