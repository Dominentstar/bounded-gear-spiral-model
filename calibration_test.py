import math

# ==============================================================================
# The Bounded Gear-Spiral & Elastic Time-Plane Model (Version 2.0)
# Numerical Calibration & Boundary Verification Script
# Author: Pranjwal Kumar Tripathy
# DOI: https://doi.org
# License: CC BY 4.0
# ==============================================================================

# Fundamental Physical & Cosmological Constants
R_0 = 4.40e26          # Observable cosmic horizon radius at Position 12 (meters)
C_LIGHT = 2.99792458e8 # Speed of light in vacuum (m/s)
H0_EARLY = 67.4        # Planck 2018 CMB Hubble constant (km/s/Mpc)
H0_LATE = 73.0         # SH0ES 2022 Type Ia Supernovae Hubble constant (km/s/Mpc)
PI = math.pi


def spiral_radius(n: float, r0: float = R_0) -> float:
    """Computes the bounded logarithmic spiral radius R(n) = R_0 * pi^(-n)."""
    return r0 * (PI ** (-n))


def gear_compression_ratio(n: float) -> float:
    """Computes the master gear-compression ratio kappa_n = pi^n = exp(n * ln(pi))."""
    return PI ** n


def effective_curvature_pi(n: float) -> float:
    """Computes progressive spatial curvature drop pi_eff(n) = pi^(1 - n/2) (Prediction 2)."""
    return PI ** (1.0 - (n / 2.0))


def young_laplace_pressure_diff(surface_tension_gamma: float, radius: float) -> float:
    """
    Computes Young-Laplace cosmic bubble boundary equilibrium (Postulate IX):
    Delta_P = P_in - P_out = 2 * gamma / R
    """
    if radius <= 0:
        raise ValueError("Radius must remain strictly positive (R_min > 0).")
    return (2.0 * surface_tension_gamma) / radius


def quasar_alpha_drift(z: float, proportionality_k: float = 1.0e-6) -> float:
    """Computes logarithmic fine-structure drift Delta_alpha / alpha_0 proportional to ln(1 + z) (Prediction 1)."""
    return proportionality_k * math.log(1.0 + z)


def harmonic_gw_frequency(n: int, f0: float = 1.0e-9) -> float:
    """Computes harmonic gravitational-wave static frequency f_n = f_0 * pi^n (Prediction 3)."""
    return f0 * (PI ** n)


def run_verification() -> None:
    print("=" * 72)
    print("THE BOUNDED GEAR-SPIRAL & ELASTIC TIME-PLANE MODEL (v2.0)")
    print("Numerical Calibration & Falsifiable Prediction Suite")
    print("=" * 72)

    # 1. Hubble Tension Discrepancy Check
    hubble_ratio = H0_LATE / H0_EARLY
    delta_n_hubble = math.log(hubble_ratio) / math.log(PI)
    print(f"\n[1] HUBBLE TENSION ANCHOR")
    print(f"    Early H0 (Planck): {H0_EARLY:.1f} km/s/Mpc | Late H0 (SH0ES): {H0_LATE:.1f} km/s/Mpc")
    print(f"    Observed Expansion Ratio (H_late / H_early): {hubble_ratio:.4f} (~{(hubble_ratio - 1)*100:.2f}%)")
    print(f"    Equivalent Inward Gear Shift (Delta n):      {delta_n_hubble:.5f} steps")

    # 2. Bounded 12 -> 1 Logarithmic Spiral Table
    print(f"\n[2] BOUNDED 12 -> 1 LOGARITHMIC SPIRAL CALIBRATION (R_0 = {R_0:.2e} m)")
    print(f"    {'Clock Pos':<10} | {'Step n':<6} | {'Radius R(n) [m]':<18} | {'Compression kappa_n':<20} | {'pi_eff(n)':<10}")
    print("    " + "-" * 74)
    for step_n in range(0, 12):
        clock_pos = 12 - step_n
        r_n = spiral_radius(step_n)
        k_n = gear_compression_ratio(step_n)
        pi_eff = effective_curvature_pi(step_n)
        print(f"    Pos {clock_pos:<6} | {step_n:<6} | {r_n:<18.4e} | {k_n:<20.4e} | {pi_eff:<10.5f}")

    # 3. Young-Laplace Cosmic Bubble Boundary Equilibrium (Postulate IX)
    print(f"\n[3] YOUNG-LAPLACE COSMIC BUBBLE EQUILIBRIUM (Postulate IX)")
    sample_gamma = 1.0e17  # Illustrative elastic membrane surface tension (N/m)
    delta_p_horizon = young_laplace_pressure_diff(sample_gamma, R_0)
    print(f"    Outer Horizon Radius (R_0):       {R_0:.2e} m")
    print(f"    Sample Surface Tension (gamma):   {sample_gamma:.2e} N/m")
    print(f"    Equilibrium Pressure (Delta P):   {delta_p_horizon:.4e} Pa (Prevents Big Rip)")

    # 4. Sample Falsifiable Predictions
    print(f"\n[4] SAMPLE FALSIFIABLE PREDICTIONS")
    for z in [0.5, 1.5, 3.0]:
        print(f"    Quasar Redshift z = {z:<4} -> Predicted Relative Drift (Delta_alpha/alpha_0): {quasar_alpha_drift(z):.4e}")
    print(f"    Harmonic GW Static (f_0 = 1 nHz, n = 2): {harmonic_gw_frequency(2):.4e} Hz")
    print("\n" + "=" * 72)


if __name__ == "__main__":
    run_verification()
