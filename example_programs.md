## Example Programs

### Hybrid Deterministic-Intelligent Program

```
#ailang
# Customer Service Automation System

DO INTELLIGENTLY process_customer_inquiry:
    # Deterministic input
    GET inquiry FROM customer_service_queue
    GET customer_history FROM database WHERE customer_id EQUALS inquiry.customer_id

    # Intelligent analysis with gaps
    INTELLIGENTLY analyze_inquiry_type FROM inquiry.text
    CONTEXTUALLY assess_urgency BASED_ON customer_history AND inquiry_content

    # Deterministic control flow
    IF urgency EQUALS "high" THEN:
        # Intelligent content generation
        CREATIVELY craft_immediate_response WITH:
            TONE: empathetic_and_professional
            CONSTRAINTS: company_policy_guidelines
            OBJECTIVE: customer_satisfaction
        END

        SEND response TO customer_email
        SEND alert TO human_supervisor

    ELSE IF inquiry_type EQUALS "technical_support" THEN:
        # Intelligent troubleshooting
        INTELLIGENTLY diagnose_technical_issue FROM inquiry.details
        ADAPTIVELY suggest_solutions BASED_ON customer_technical_level

        SEND troubleshooting_guide TO customer_email

    ELSE:
        # Standard processing
        SET response TO generate_standard_response(inquiry_type)
        SEND response TO customer_email
    END_IF

    # Deterministic logging
    SET inquiry.status TO "processed"
    SET inquiry.processed_time TO current_time
    SEND inquiry TO processed_inquiries_log
END
```

### Data Analysis with Intelligent Insights

```
#ailang
DO analyze_sales_performance:
    # Deterministic data retrieval
    GET sales_data FROM "quarterly_sales.csv"
    GET previous_quarter FROM "previous_quarter.csv"

    # Intelligent data processing
    INTELLIGENTLY clean_and_validate sales_data
    CONTEXTUALLY identify_trends AND patterns

    # Deterministic calculations
    SET current_total TO 0
    FOR EACH sale IN sales_data DO:
        SET current_total TO current_total + sale.amount
    END_FOR

    SET previous_total TO 0
    FOR EACH sale IN previous_quarter DO:
        SET previous_total TO previous_total + sale.amount
    END_FOR

    SET growth_rate TO (current_total - previous_total) / previous_total * 100

    # Intelligent insights generation
    CREATIVELY generate_insights FROM:
        DATA: sales_data, previous_quarter
        METRICS: current_total, growth_rate
        CONTEXT: market_conditions, seasonal_factors
    END

    # Deterministic output
    CREATE OBJECT report:
        total_sales: current_total
        growth_rate: growth_rate
        insights: generated_insights
        generated_date: current_time
    END_OBJECT

    SEND report TO "quarterly_report.json"
    SEND executive_summary TO management_team
END
```

### Extended Example Programs with Mathematics

#### Nested Mathematical Contexts

```
#ailang
WITH MATHEMATICAL_CONTEXT:
    DOMAIN: real
    PRECISION: standard
    
    # Real number calculations
    SET distance TO sqrt(x^2 + y^2)
    
    # Need complex numbers for a specific calculation
    WITH MATHEMATICAL_CONTEXT:
        DOMAIN: complex
        PRECISION: high
        
        # Complex operations
        SET phase TO e^(i*theta)
        SET amplitude TO |phase|
        
    END_CONTEXT
    
    # Back to real domain
    SET final_result TO distance * 2
    
END_CONTEXT
```

#### Example: Black-Scholes Option Pricing

```
#ailang
# Black-Scholes Option Pricing Model
WITH MATHEMATICAL_CONTEXT:
    DOMAIN: real
    PRECISION: high
    CONSTRAINTS: [S > 0, K > 0, r >= 0, T > 0, sigma > 0]

    DEFINE PROCEDURE black_scholes_call WITH PARAMETERS [S, K, r, T, sigma]:
        # Validate parameters
        ASSERT S > 0 "Stock price must be positive"
        ASSERT K > 0 "Strike price must be positive"
        ASSERT T > 0 "Time to maturity must be positive"
        ASSERT sigma > 0 "Volatility must be positive"
        ASSERT r >= 0 "Risk-free rate must be non-negative"
        
        # S = current stock price
        # K = strike price
        # r = risk-free rate
        # T = time to maturity
        # sigma = volatility
        
        # Calculate d1 and d2
        SET d1 TO (ln(S/K) + (r + sigma²/2)*T) / (sigma*sqrt(T))
        SET d2 TO d1 - sigma*sqrt(T)
        
        # Standard normal cumulative distribution
        SET N_d1 TO CUMULATIVE_NORMAL(d1)
        SET N_d2 TO CUMULATIVE_NORMAL(d2)
        
        # Black-Scholes formula
        SET call_price TO S*N_d1 - K*e^(-r*T)*N_d2
        
        # Calculate Greeks
        SET delta TO N_d1
        SET gamma TO NORMAL_PDF(d1) / (S*sigma*sqrt(T))
        SET theta TO -(S*NORMAL_PDF(d1)*sigma)/(2*sqrt(T)) - r*K*e^(-r*T)*N_d2
        SET vega TO S*NORMAL_PDF(d1)*sqrt(T)
        SET rho TO K*T*e^(-r*T)*N_d2
        
        RETURN {
            price: call_price,
            delta: delta,
            gamma: gamma,
            theta: theta,
            vega: vega,
            rho: rho
        }
        
        # Call the procedure within the same context
        SET option_value TO CALL black_scholes_call WITH [100, 110, 0.05, 0.25, 0.20]
    
END_CONTEXT

# Example usage
SET option_value TO CALL black_scholes_call WITH [100, 110, 0.05, 0.25, 0.20]
SEND option_value TO display
```

#### Example: Quantum Harmonic Oscillator
```
#ailang
# Quantum Harmonic Oscillator Energy Levels and Wavefunctions
MATHEMATICAL_CONTEXT:
    DOMAIN: complex
    PRECISION: symbolic

    DEFINE PROCEDURE quantum_harmonic_oscillator WITH PARAMETERS [n, x, m, omega, hbar]:
        # n = quantum number
        # x = position
        # m = mass
        # omega = angular frequency
        # hbar = reduced Planck constant
        
        # Define Hamiltonian operator
        SET hamiltonian TO -(hbar^2/(2*m)) * d²/dx² + (1/2)*m*omega^2*x^2
        
        # Calculate energy level
        SET E_n TO hbar*omega*(n + 1/2)
        
        # Calculate characteristic length
        SET x_0 TO sqrt(hbar/(m*omega))
        
        # Hermite polynomial H_n
        SET H_n TO HERMITE_POLYNOMIAL(n, x/x_0)
        
        # Wavefunction
        SET normalization TO 1/sqrt(2^n * factorial(n)) * (m*omega/(pi*hbar))^(1/4)
        SET gaussian TO e^(-(x²)/(2*x_0²))
        SET psi_n TO normalization * H_n * gaussian
        
        # Probability density
        SET probability_density TO |psi_n|²
        
        # Expectation values
        SET position_expectation TO INTEGRATE x * probability_density FROM -infinity TO infinity
        SET momentum_expectation TO 0  # Always zero for energy eigenstates
        SET position_uncertainty TO sqrt(INTEGRATE x² * probability_density FROM -infinity TO infinity)
        SET momentum_uncertainty TO sqrt((n + 1/2) * hbar * m * omega)
        
        # Verify uncertainty principle
        SET uncertainty_product TO position_uncertainty * momentum_uncertainty
        ASSERT uncertainty_product >= hbar/2
        
        RETURN {
            energy: E_n,
            wavefunction: psi_n,
            probability_density: probability_density,
            uncertainties: {
                position: position_uncertainty,
                momentum: momentum_uncertainty,
                product: uncertainty_product
            }
        }
    
END_CONTEXT
```

#### Example: Fluid Dynamics Simulation

```
#ailang
# Navier-Stokes Equation Solver for 2D Incompressible Flow
MATHEMATICAL_CONTEXT:
    DOMAIN: real
    PRECISION: high

    DEFINE PROCEDURE navier_stokes_2d WITH PARAMETERS [u0, v0, p0, viscosity, dt, dx, dy]:
        # u0, v0 = initial velocity field components
        # p0 = initial pressure field
        # viscosity = kinematic viscosity
        
        # Momentum equations with incompressibility constraint
        SOLVE_PDE_SYSTEM:
            # x-momentum
            ∂u/∂t + u*∂u/∂x + v*∂u/∂y = -1/ρ * ∂p/∂x + viscosity*(∂²u/∂x² + ∂²u/∂y²)
            
            # y-momentum  
            ∂v/∂t + u*∂v/∂x + v*∂v/∂y = -1/ρ * ∂p/∂y + viscosity*(∂²v/∂x² + ∂²v/∂y²)
            
            # Continuity (incompressibility)
            ∂u/∂x + ∂v/∂y = 0
            
            INITIAL_CONDITIONS: u = u0, v = v0, p = p0
            BOUNDARY_CONDITIONS: no_slip_walls
            METHOD: projection_method
            TIME_STEP: dt
            SPATIAL_STEP: [dx, dy]
        END_SOLVE
        
        # Calculate derived quantities
        SET vorticity TO CURL([u, v])
        SET stream_function TO SOLVE_POISSON(∂²ψ/∂x² + ∂²ψ/∂y² = -vorticity)
        SET kinetic_energy TO INTEGRATE 0.5*(u² + v²) OVER_DOMAIN
        
        # Check CFL condition for stability
        SET max_velocity TO MAX(sqrt(u² + v²))
        SET CFL_number TO max_velocity * dt / MIN(dx, dy)
        IF CFL_number > 1 THEN:
            WARN "Simulation may be unstable: CFL = " + CFL_number
        END_IF
        
        RETURN {
            velocity_field: [u, v],
            pressure: p,
            vorticity: vorticity,
            stream_function: stream_function,
            kinetic_energy: kinetic_energy,
            CFL: CFL_number
        }
    
END_CONTEXT
```

#### Example: Machine Learning Gradient Descent

```
#ailang
# Neural Network Training with Backpropagation
MATHEMATICAL_CONTEXT:
    DOMAIN: real
    PRECISION: high

    DEFINE PROCEDURE train_neural_network WITH PARAMETERS [X, y, architecture, learning_rate]:
        # Set regularization strength
        SET lambda TO 0.0001  # L2 regularization parameter
        
        # Initialize weights with Xavier initialization
        SET weights TO []
        FOR EACH layer IN architecture DO:
            SET W TO RANDOM_NORMAL(0, sqrt(2/layer.input_size))
            APPEND W TO weights
        END_FOR
        
        # Training loop
        REPEAT 1000 TIMES:
            # Forward propagation
            SET activations TO [X]
            FOR EACH W IN weights DO:
                SET z TO MATRIX_MULTIPLY(activations[-1], W)
                SET a TO RELU(z)  # or other activation function
                APPEND a TO activations
            END_FOR
            
            # Calculate loss (mean squared error)
            SET predictions TO activations[-1]
            SET loss TO MEAN((predictions - y)²)
            
            # Backward propagation
            SET gradients TO []
            SET delta TO 2*(predictions - y) / SIZE(y)
            
            FOR layer FROM last TO first DO:
                # Gradient with respect to weights
                SET grad_W TO MATRIX_MULTIPLY(TRANSPOSE(activations[layer]), delta)
                PREPEND grad_W TO gradients
                
                # Propagate error backward
                IF layer > 0 THEN:
                    SET delta TO MATRIX_MULTIPLY(delta, TRANSPOSE(weights[layer]))
                    SET delta TO delta * RELU_DERIVATIVE(activations[layer])
                END_IF
            END_FOR
            
            # Update weights using gradient descent
            FOR i FROM 0 TO LENGTH(weights) DO:
                SET weights[i] TO weights[i] - learning_rate * gradients[i]
                
                # Optional: Add L2 regularization
                SET weights[i] TO weights[i] - learning_rate * lambda * weights[i]
            END_FOR
            
            # Check convergence
            IF loss < 0.001 THEN:
                BREAK
            END_IF
        END_REPEAT
        
        RETURN {
            trained_weights: weights,
            final_loss: loss
        }

END_CONTEXT
```

#### Example: Advanced Financial Options Pricing with Nested Integration

```
#ailang
# American Option Pricing using Nested Integration and Conditional Logic
MATHEMATICAL_CONTEXT:
    DOMAIN: real
    PRECISION: high
    
    DEFINE PROCEDURE price_american_option WITH PARAMETERS [S0, K, r, sigma, T, option_type]:
        # American options can be exercised early - requires nested conditional integration
        
        # Define the optimal exercise boundary (free boundary problem)
        DEFINE FUNCTION exercise_boundary(t):
            # Solve for S*(t) where it's optimal to exercise
            SOLVE_IMPLICIT:
                EQUATION: option_value(S_star, t) = intrinsic_value(S_star)
                WHERE intrinsic_value = IF option_type = "call" THEN:
                    MAX(S_star - K, 0)
                ELSE:
                    MAX(K - S_star, 0)
                END_IF
            END_SOLVE
            RETURN S_star
        END_FUNCTION
        
        # Price using integral representation with early exercise
        SET option_price TO INTEGRATE (
            # Outer integral over all possible stock prices at maturity
            INTEGRATE (
                # Inner integral over all possible early exercise times
                IF S_t > exercise_boundary(t) AND option_type = "call" THEN:
                    # Continue holding the option
                    e^(-r*t) * (
                        INTEGRATE (
                            payoff(S_T) * transition_density(S_T | S_t)
                        ) FROM 0 TO infinity WITH_RESPECT_TO S_T
                    )
                ELSE IF S_t < exercise_boundary(t) AND option_type = "put" THEN:
                    # Continue holding the put option
                    e^(-r*t) * (
                        INTEGRATE (
                            payoff(S_T) * transition_density(S_T | S_t)
                        ) FROM 0 TO infinity WITH_RESPECT_TO S_T
                    )
                ELSE:
                    # Exercise immediately
                    e^(-r*t) * intrinsic_value(S_t)
                END_IF
            ) FROM 0 TO T WITH_RESPECT_TO t
        ) FROM 0 TO infinity WITH_RESPECT_TO S_t
        
        # Calculate Greeks using nested differentiation
        SET delta TO DIFFERENTIATE option_price WITH_RESPECT_TO S0
        
        SET gamma TO DIFFERENTIATE (
            DIFFERENTIATE option_price WITH_RESPECT_TO S0
        ) WITH_RESPECT_TO S0
        
        # Vega involves differentiating an integral containing sigma
        SET vega TO DIFFERENTIATE (
            INTEGRATE (
                payoff * normal_density((ln(S/S0) - (r-sigma^2/2)*t)/(sigma*sqrt(t)))
            ) FROM 0 TO infinity
        ) WITH_RESPECT_TO sigma
        
        # Theta with conditional early exercise
        SET theta TO DIFFERENTIATE (
            IF t < optimal_exercise_time THEN:
                holding_value(t)
            ELSE:
                exercise_value(t)
            END_IF
        ) WITH_RESPECT_TO t
        
        RETURN {
            price: option_price,
            delta: delta,
            gamma: gamma,
            vega: vega,
            theta: theta,
            exercise_boundary: exercise_boundary
        }
    END_PROCEDURE
    
    # Exotic Option with Path-Dependent Nested Integration
    DEFINE PROCEDURE price_asian_barrier_option WITH PARAMETERS [S0, K, H, r, sigma, T, n_averaging]:
        # Asian option with barrier - payoff depends on average and barrier hitting
        
        # Price using nested Monte Carlo integration
        SET price TO MONTE_CARLO_INTEGRATE (
            # Outer integration - over all paths
            SET path_sum TO 0
            SET barrier_hit TO false
            
            FOR t FROM 0 TO T STEP dt DO:
                SET S_t TO S_prev * exp((r - sigma^2/2)*dt + sigma*sqrt(dt)*RANDOM_NORMAL())
                
                # Check barrier condition
                IF S_t >= H THEN:
                    SET barrier_hit TO true
                END_IF
                
                # Accumulate for averaging
                IF t IN averaging_dates THEN:
                    SET path_sum TO path_sum + S_t
                END_IF
            END_FOR
            
            # Conditional payoff based on barrier and average
            IF barrier_hit THEN:
                RETURN 0  # Knock-out barrier hit
            ELSE:
                SET average TO path_sum / n_averaging
                RETURN e^(-r*T) * MAX(average - K, 0)
            END_IF
        ) OVER n_paths = 100000
        
        RETURN price
    END_PROCEDURE

END_CONTEXT
```

#### Example: Quantum Field Theory with Nested Path Integrals

```
#ailang
# Feynman Path Integral Formulation with Conditional Actions
MATHEMATICAL_CONTEXT:
    DOMAIN: complex
    PRECISION: symbolic

    DEFINE PROCEDURE quantum_path_integral WITH PARAMETERS [initial_state, final_state, lagrangian]:
        # Path integral: ∫D[x(t)] exp(iS[x]/ℏ) where S is the action
        
        # Discretize paths and integrate over all possible trajectories
        SET amplitude TO PATH_INTEGRATE (
            # Action functional with conditional potential
            SET action TO INTEGRATE (
                lagrangian(x, dx/dt, t) WHERE:
                    lagrangian = IF in_potential_well(x) THEN:
                        0.5*m*(dx/dt)^2 - V_well(x)
                    ELSE IF in_barrier_region(x) THEN:
                        0.5*m*(dx/dt)^2 - V_barrier(x) + 
                        i*GAMMA*tunneling_rate(x)  # Complex potential for tunneling
                    ELSE:
                        0.5*m*(dx/dt)^2  # Free particle
                    END_IF
            ) FROM t_initial TO t_final WITH_RESPECT_TO t
            
            # Weight by exponential of action
            SET weight TO e^(i*action/hbar)
            
            # Conditional boundary constraints
            IF satisfies_boundary_conditions(path) THEN:
                RETURN weight * transition_amplitude(path)
            ELSE:
                RETURN 0
            END_IF
        ) OVER all_paths FROM initial_state TO final_state
        
        # Normalize and extract observables
        SET norm TO PATH_INTEGRATE |weight|^2 OVER all_paths
        SET normalized_amplitude TO amplitude / sqrt(norm)
        
        # Calculate expectation values using functional derivatives
        SET position_expectation TO FUNCTIONAL_DERIVATIVE (
            ln(amplitude)
        ) WITH_RESPECT_TO source_field AT source=0
        
        # Vacuum-to-vacuum amplitude with interactions
        SET vacuum_persistence TO PATH_INTEGRATE (
            exp(i * INTEGRATE (
                L_0 + L_int WHERE:
                    L_int = IF coupling_on THEN:
                        SUM(n=2 TO 4) OF (
                            g_n/n! * phi^n
                        )
                    ELSE:
                        0
                    END_IF
            ) FROM -infinity TO infinity)
        ) OVER field_configurations
        
        RETURN {
            transition_amplitude: normalized_amplitude,
            vacuum_persistence: vacuum_persistence,
            position_expectation: position_expectation
        }

END_CONTEXT
```

#### Example: Climate Model with Nested Integration Over Time and Space

```
#ailang
# Global Climate Model with Conditional Feedback Loops
DEFINE PROCEDURE climate_system_evolution WITH PARAMETERS [initial_conditions, forcing_scenarios]:
    
    # Temperature evolution with nested spatial and temporal integration
    SET global_temperature TO SOLVE_PDE:
        # Heat equation with conditional feedbacks
        ∂T/∂t = DIVERGENCE(k*GRADIENT(T)) + 
        INTEGRATE (
            # Integrate over all atmospheric layers
            SUM(layer=1 TO n_layers) OF (
                IF T[layer] > freezing_point THEN:
                    # Water vapor feedback (positive)
                    alpha_wv * (
                        INTEGRATE humidity_response(T, p) 
                        FROM surface TO tropopause
                    )
                ELSE:
                    # Ice-albedo feedback (positive)
                    alpha_ice * DIFFERENTIATE albedo WITH_RESPECT_TO ice_coverage
                END_IF
            )
        ) OVER atmospheric_column +
        INTEGRATE (
            # Ocean heat uptake (conditional on circulation)
            IF atlantic_circulation > threshold THEN:
                INTEGRATE heat_flux FROM surface TO thermocline
            ELSE:
                # Weakened circulation - different heat distribution
                INTEGRATE modified_heat_flux FROM surface TO mixed_layer_depth
            END_IF
        ) OVER ocean_basins
    END_SOLVE
    
    # Carbon cycle with conditional sinks and sources
    SET atmospheric_co2 TO INTEGRATE (
        # Emissions
        emissions(t) -
        # Ocean uptake (temperature-dependent)
        INTEGRATE (
            IF ocean_T < saturation_T(pCO2) THEN:
                k_ocean * (pCO2_atm - pCO2_ocean)
            ELSE:
                0  # Ocean becomes source above saturation
            END_IF
        ) OVER ocean_surface -
        # Land uptake (conditional on temperature and moisture)
        INTEGRATE (
            IF T_soil > 0 AND T_soil < 35 AND moisture > wilting_point THEN:
                # Photosynthesis minus respiration
                GPP(T, CO2, light) - (
                    INTEGRATE respiration(T, depth) FROM 0 TO soil_depth
                )
            ELSE IF T_soil > 35 OR moisture < wilting_point THEN:
                -stress_emissions  # Vegetation stress causes emissions
            ELSE:
                # Frozen soil - minimal exchange
                permafrost_flux(T_soil)
            END_IF
        ) OVER land_surface
    ) FROM t0 TO t WITH_RESPECT_TO time
    
    # Sea level rise with multiple nested components
    SET sea_level_change TO SUM OF:
        # Thermal expansion
        INTEGRATE (
            INTEGRATE (
                alpha_thermal(T, S, p) * dT
            ) FROM surface TO ocean_bottom
        ) OVER all_oceans,
        
        # Ice sheet contribution (with threshold behavior)
        INTEGRATE (
            IF surface_T > melt_threshold THEN:
                # Surface melting
                INTEGRATE melt_rate(T) OVER ice_sheet_surface
            ELSE:
                0
            END_IF +
            IF ocean_T > grounding_line_T THEN:
                # Basal melting and calving
                INTEGRATE (
                    basal_melt_rate(ocean_T, salinity)
                ) ALONG grounding_line
            ELSE:
                background_calving_rate
            END_IF
        ) FROM t0 TO t,
        
        # Mountain glaciers (elevation-dependent)
        SUM(glacier IN all_glaciers) OF (
            INTEGRATE (
                IF elevation < equilibrium_line_altitude(t) THEN:
                    # Below ELA - melting
                    INTEGRATE melt(T, elevation) OVER glacier_area(elevation)
                ELSE:
                    # Above ELA - accumulation
                    -INTEGRATE accumulation(precip, T) OVER glacier_area(elevation)
                END_IF
            ) FROM base TO summit
        )
    END_SUM
    
    # Tipping point detection using derivatives of integrated quantities
    SET tipping_indicators TO {
        arctic_ice_tipping: DIFFERENTIATE (
            INTEGRATE ice_volume OVER arctic
        ) WITH_RESPECT_TO time < critical_rate,
        
        amazon_dieback: DIFFERENTIATE (
            INTEGRATE (
                IF precipitation < critical_precip FOR duration > 2_years THEN:
                    forest_fraction
                ELSE:
                    1
                END_IF
            ) OVER amazon_basin
        ) WITH_RESPECT_TO time,
        
        permafrost_collapse: SECOND_DERIVATIVE (
            INTEGRATE (
                IF ground_T > 0 THEN:
                    carbon_release_rate(T, depth)
                ELSE:
                    0
                END_IF
            ) FROM surface TO permafrost_depth
        ) WITH_RESPECT_TO time > acceleration_threshold
    }
    
    RETURN {
        temperature_projection: global_temperature,
        co2_trajectory: atmospheric_co2,
        sea_level_rise: sea_level_change,
        tipping_points: tipping_indicators,
        uncertainty_bounds: monte_carlo_confidence_intervals
    }
END_PROCEDURE
```

#### Example: Advanced Radar System for Aircraft Detection and Tracking

```
#ailang
# Advanced Radar System for Aircraft Detection and Tracking
# Demonstrates extensive use of i and trigonometry

MATHEMATICAL_CONTEXT:
    DOMAIN: complex
    PRECISION: high

    DEFINE PROCEDURE process_radar_signal WITH PARAMETERS [raw_signal, carrier_freq, sample_rate, c, antenna_spacing]:
        # Radar uses complex I/Q (In-phase/Quadrature) signals
        # c = speed of light (typically 299792458 m/s)
        
        SET speed_of_light TO c
        SET wavelength TO speed_of_light / carrier_freq
        
        # Step 1: Demodulate received signal to baseband using complex exponential
        SET t TO LINSPACE(0, LENGTH(raw_signal)/sample_rate, LENGTH(raw_signal))
        SET demodulation_signal TO e^(-i*2*pi*carrier_freq*t)
        SET baseband_signal TO raw_signal * demodulation_signal
        
        # Step 2: Apply matched filter (pulse compression)
        # Transmitted chirp: s(t) = e^(i*pi*α*t²) where α is chirp rate
        SET chirp_rate TO 1e12  # Hz/s
        SET matched_filter TO CONJUGATE(e^(i*pi*chirp_rate*t^2))
        SET compressed_signal TO CONVOLVE(baseband_signal, matched_filter)
        
        # Step 3: Range-Doppler processing using 2D FFT
        # Arrange data into range-Doppler matrix
        SET range_bins TO 512
        SET doppler_bins TO 256
        SET data_matrix TO RESHAPE(compressed_signal, [range_bins, doppler_bins])
        
        # First FFT for range processing
        FOR EACH column IN data_matrix DO:
            SET range_fft TO CALL fast_fourier_transform WITH [column]
            SET data_matrix[column] TO range_fft
        END_FOR
        
        # Second FFT for Doppler processing
        FOR EACH row IN data_matrix DO:
            SET doppler_fft TO CALL fast_fourier_transform WITH [row]
            SET data_matrix[row] TO doppler_fft
        END_FOR
        
        # Step 4: Convert to polar coordinates for target detection
        SET range_doppler_map TO |data_matrix|^2  # Power spectrum
        
        # Step 5: Target detection using CFAR (Constant False Alarm Rate)
        SET noise_floor TO MEAN(range_doppler_map)
        SET threshold TO noise_floor * 10^(12/10)  # 12 dB above noise
        
        SET targets TO []
        FOR r FROM 0 TO range_bins-1 DO:
            FOR d FROM 0 TO doppler_bins-1 DO:
                IF range_doppler_map[r,d] > threshold THEN:
                    # Convert bin indices to physical units
                    SET range TO r * speed_of_light / (2 * sample_rate)
                    SET velocity TO d * speed_of_light * carrier_freq / (2 * doppler_bins * sample_rate)
                    
                    # Extract phase for angle measurement (monopulse)
                    SET phase TO ARG(data_matrix[r,d])
                    
                    # Monopulse processing for angle estimation
                    # Note: simplified monopulse - actual implementation requires antenna array geometry
                    SET azimuth TO arcsin(phase / (2*pi * antenna_spacing / wavelength))
                    SET elevation TO arcsin(phase / (2*pi * antenna_spacing / wavelength))  # Simplified
                    
                    APPEND {
                        range: range,
                        velocity: velocity, 
                        azimuth: azimuth,  # Keep in radians for internal processing
                        elevation: elevation,  # Keep in radians for internal processing
                        azimuth_deg: DEGREES(azimuth),  # Degrees for display
                        elevation_deg: DEGREES(elevation),  # Degrees for display
                        snr: 10*log10(range_doppler_map[r,d] / noise_floor)
                    } TO targets
                END_IF
            END_FOR
        END_FOR
        
        # Step 6: Kalman filtering for tracking (uses complex state space)
        # Initialize Kalman filter matrices
        SET measurement_noise TO 10  # Measurement uncertainty
        SET P TO IDENTITY(6) * 100  # Initial covariance
        SET H TO OBSERVATION_MATRIX(3, 6)  # Maps state to measurements
        SET R TO IDENTITY(3) * measurement_noise  # Measurement noise covariance
        
        FOR EACH target IN targets DO:
            # State vector: [x, y, z, vx, vy, vz]
            # Convert from polar to Cartesian for state representation
            SET x TO target.range * cos(target.elevation) * cos(target.azimuth)
            SET y TO target.range * cos(target.elevation) * sin(target.azimuth)
            SET z TO target.range * sin(target.elevation)
            
            # Velocity vector from Doppler (radial) and estimated tangential components
            SET radial_velocity TO target.velocity  # From Doppler
            SET state TO [x, y, z, radial_velocity, 0, 0]  # Initialize with radial velocity
            
            # Predict next position
            SET dt TO 0.1  # 100ms update rate
            SET predicted_state TO state + [state[3]*dt, state[4]*dt, state[5]*dt, 0, 0, 0]
            
            # Innovation using complex measurements
            SET measurement TO target.range * e^(i*target.azimuth)
            SET innovation TO measurement - predicted_state
            
            # Update with complex Kalman gain
            SET kalman_gain TO P*H' / (H*P*H' + R)
            SET updated_state TO predicted_state + kalman_gain * innovation
            
            SET target.predicted_position TO updated_state
        END_FOR
        
        RETURN {
            targets: targets,
            range_doppler_map: range_doppler_map,
            detection_performance: {
                # Note: simplified detection models - actual performance depends on many factors
                cfar_threshold: threshold,
                estimated_pfa: 1e-6  # Typical CFAR design target
            }
        }
    END_PROCEDURE
    
    # Phased Array Beamforming with Complex Weights
    DEFINE PROCEDURE beamform_phased_array WITH PARAMETERS [element_signals, steering_angle, carrier_frequency]:
        SET n_elements TO LENGTH(element_signals)
        SET speed_of_light TO 299792458  # m/s
        SET wavelength TO speed_of_light / carrier_frequency
        SET element_spacing TO wavelength / 2  # Half wavelength spacing
        
        # Calculate complex beamforming weights using trigonometry
        SET weights TO []
        FOR n FROM 0 TO n_elements-1 DO:
            # Progressive phase shift for beam steering
            SET phase_shift TO 2*pi * element_spacing * n * sin(steering_angle) / wavelength
            SET weight TO e^(-i*phase_shift)  # Complex weight
            APPEND weight TO weights
        END_FOR
        
        # Apply weights and sum (complex multiplication)
        SET beamformed_signal TO 0 + 0*i
        FOR n FROM 0 TO n_elements-1 DO:
            SET beamformed_signal TO beamformed_signal + element_signals[n] * weights[n]
        END_FOR
        
        # Calculate beam pattern
        SET angles TO LINSPACE(-pi/2, pi/2, 360)
        SET beam_pattern TO []
        FOR theta IN angles DO:
            SET array_factor TO 0 + 0*i
            FOR n FROM 0 TO n_elements-1 DO:
                SET phase TO 2*pi * element_spacing * n * sin(theta) / wavelength
                SET array_factor TO array_factor + weights[n] * e^(i*phase)
            END_FOR
            APPEND 20*log10(|array_factor|) TO beam_pattern  # dB scale
        END_FOR
        
        # Calculate beam characteristics
        SET main_lobe_width TO 2*arcsin(wavelength / (n_elements * element_spacing))  # Approximate
        SET max_sidelobe TO MAX(beam_pattern WHERE |angle - steering_angle| > main_lobe_width)
        
        RETURN {
            output_signal: beamformed_signal,
            beam_pattern: beam_pattern,
            main_lobe_width_deg: DEGREES(main_lobe_width),
            sidelobe_level_dB: max_sidelobe,
            array_gain_dB: 10*log10(n_elements)
        }
    END_PROCEDURE    

END_CONTEXT

```

#### Example: Quantum Circuit Simulation with Complex Amplitudes

```
#ailang
# Quantum Computing Circuit Simulator
# Heavily uses i for quantum amplitudes and trigonometry for gate rotations

DEFINE PROCEDURE simulate_quantum_circuit WITH PARAMETERS [n_qubits, gates]:
    # Initialize quantum state in |000...0⟩
    SET state_size TO 2^n_qubits
    SET quantum_state TO ZEROS(state_size) + 0*i  # Complex state vector
    SET quantum_state[0] TO 1 + 0*i  # |000...0⟩ state
    
    # Define quantum gates using complex matrices
    SET pauli_x TO [[0, 1], [1, 0]]  # NOT gate
    SET pauli_y TO [[0, -i], [i, 0]]  # Y gate  
    SET pauli_z TO [[1, 0], [0, -1]]  # Z gate
    SET hadamard TO [[1, 1], [1, -1]] / sqrt(2)  # Superposition
    
    # Process each gate in the circuit
    FOR EACH gate IN gates DO:
        MATCH gate.type WITH:
            CASE "hadamard":
                SET matrix TO hadamard
                
            CASE "phase":
                # Phase gate: R(θ) = [[1, 0], [0, e^(iθ)]]
                SET matrix TO [[1, 0], [0, e^(i*gate.angle)]]
                
            CASE "rotation_x":
                # Rotation around X-axis
                SET matrix TO [
                    [cos(gate.angle/2), -i*sin(gate.angle/2)],
                    [-i*sin(gate.angle/2), cos(gate.angle/2)]
                ]
                
            CASE "rotation_y":
                # Rotation around Y-axis
                SET matrix TO [
                    [cos(gate.angle/2), -sin(gate.angle/2)],
                    [sin(gate.angle/2), cos(gate.angle/2)]
                ]
                
            CASE "rotation_z":
                # Rotation around Z-axis
                SET matrix TO [
                    [e^(-i*gate.angle/2), 0],
                    [0, e^(i*gate.angle/2)]
                ]
                
            CASE "cnot":
                # Controlled-NOT gate (entanglement)
                SET matrix TO [
                    [1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 1],
                    [0, 0, 1, 0]
                ]
                
            CASE "toffoli":
                # Toffoli gate (universal reversible)
                SET matrix TO IDENTITY(8)
                SET matrix[6,6] TO 0
                SET matrix[6,7] TO 1
                SET matrix[7,6] TO 1
                SET matrix[7,7] TO 0
                
            CASE "qft":
                # Quantum Fourier Transform
                SET matrix TO []
                SET N TO 2^gate.n_qubits
                FOR j FROM 0 TO N-1 DO:
                    SET row TO []
                    FOR k FROM 0 TO N-1 DO:
                        SET omega TO e^(2*pi*i*j*k/N)
                        APPEND omega/sqrt(N) TO row
                    END_FOR
                    APPEND row TO matrix
                END_FOR
        END_MATCH
        
        # Apply gate to quantum state
        SET quantum_state TO APPLY_GATE(matrix, quantum_state, gate.target_qubits)
    END_FOR
    
    # Measure probabilities (Born rule: |ψ|²)
    SET probabilities TO []
    FOR EACH amplitude IN quantum_state DO:
        SET probability TO |amplitude|^2  # |complex amplitude|²
        APPEND probability TO probabilities
    END_FOR
    
    # Calculate entanglement entropy using complex amplitudes
    SET entropy TO 0
    FOR EACH p IN probabilities WHERE p > 0 DO:
        SET entropy TO entropy - p * log2(p)
    END_FOR
    
    # Phase estimation
    SET global_phase TO ARG(quantum_state[0])
    SET relative_phases TO []
    FOR EACH amplitude IN quantum_state DO:
        IF |amplitude| > 1e-10 THEN:
            SET relative_phase TO ARG(amplitude) - global_phase
            APPEND MOD(relative_phase, 2*pi) TO relative_phases
        END_IF
    END_FOR
    
    RETURN {
        final_state: quantum_state,
        probabilities: probabilities,
        entropy: entropy,
        phases: relative_phases
    }
END_PROCEDURE

# Shor's Algorithm Implementation using Complex Arithmetic
DEFINE PROCEDURE shors_algorithm WITH PARAMETERS [N_to_factor]:
    # Quantum period finding using complex exponentials
    
    # Choose random a < N
    SET a TO RANDOM_INT(2, N_to_factor-1)
    
    # Check if gcd(a,N) > 1 (classical)
    SET g TO GCD(a, N_to_factor)
    IF g > 1 THEN:
        RETURN {factor1: g, factor2: N_to_factor/g}
    END_IF
    
    # Quantum period finding
    SET n_qubits TO CEIL(log2(N_to_factor))
    SET register1 TO SUPERPOSITION(n_qubits)  # Equal superposition
    SET register2 TO ZEROS(n_qubits)
    
    # Modular exponentiation (quantum)
    FOR EACH basis_state IN register1 DO:
        SET value TO a^basis_state MOD N_to_factor
        # Entangle with complex phase
        SET phase TO e^(2*pi*i*basis_state/N_to_factor)
        SET register2 TO register2 + phase * |value⟩
    END_FOR
    
    # Apply Quantum Fourier Transform
    SET qft_state TO []
    SET Q TO 2^n_qubits
    FOR k FROM 0 TO Q-1 DO:
        SET amplitude TO 0 + 0*i
        FOR j FROM 0 TO Q-1 DO:
            SET omega TO e^(2*pi*i*j*k/Q)
            SET amplitude TO amplitude + register1[j] * omega
        END_FOR
        APPEND amplitude/sqrt(Q) TO qft_state
    END_FOR
    
    # Measure and extract period using continued fractions
    SET measurement TO MEASURE(qft_state)
    SET period TO EXTRACT_PERIOD_FROM_QFT(measurement, N_to_factor)
    
    # Classical post-processing
    IF period IS_EVEN AND a^(period/2) ≠ -1 MOD N_to_factor THEN:
        SET factor1 TO GCD(a^(period/2) - 1, N_to_factor)
        SET factor2 TO GCD(a^(period/2) + 1, N_to_factor)
        
        IF factor1 * factor2 = N_to_factor THEN:
            RETURN {factor1: factor1, factor2: factor2, period: period}
        END_IF
    END_IF
    
    # Retry if failed
    RETURN CALL shors_algorithm WITH [N_to_factor]
END_PROCEDURE
```

#### Example: Electromagnetic Wave Propagation

```
#ailang
# Maxwell's Equations Solver using Complex Fields and Trigonometry
MATHEMATICAL_CONTEXT:
    DOMAIN: complex
    PRECISION: high

    DEFINE PROCEDURE solve_maxwell_equations WITH PARAMETERS [E0, B0, boundary, frequency, medium]:
        # Physical constants
        SET speed_of_light TO 299792458  # m/s
        SET epsilon_0 TO 8.854187817e-12  # Permittivity of free space
        SET mu_0 TO 1.256637061e-6  # Permeability of free space
        SET impedance_0 TO sqrt(mu_0/epsilon_0)  # Free space impedance ~377 ohms
        
        # Medium parameters (default to free space if not specified)
        SET mu TO medium.mu IF medium.mu EXISTS ELSE mu_0
        SET epsilon TO medium.epsilon IF medium.epsilon EXISTS ELSE epsilon_0
        SET sigma TO medium.conductivity IF medium.conductivity EXISTS ELSE 0
        
        # Electric and magnetic fields as complex phasors
        # E(r,t) = Re[Ẽ(r) * e^(-iωt)]
        # B(r,t) = Re[B̃(r) * e^(-iωt)]
        
        SET omega TO 2*pi*frequency
        SET k TO omega/speed_of_light  # Wave number
        SET wavelength TO 2*pi/k
        
        # Solve Helmholtz equation for electric field
        # ∇²Ẽ + k²Ẽ = 0
        SOLVE_PDE:
            EQUATION: ∂²E/∂x² + ∂²E/∂y² + ∂²E/∂z² + k²*E = 0
            BOUNDARY_CONDITIONS: boundary
            DOMAIN: computational_domain
        END_SOLVE AS E_field
        
        # Calculate magnetic field from electric field
        # B̃ = (i/ω) * ∇ × Ẽ
        SET B_field TO (i/omega) * CURL(E_field)
        
        # Source terms (if present)
        SET rho TO boundary.charge_density  # Charge density
        SET J TO boundary.current_density  # Current density
        
        # Verify Maxwell's equations in complex form
        ASSERT DIVERGENCE(E_field) EQUALS rho/epsilon_0  # Gauss's law
        ASSERT DIVERGENCE(B_field) EQUALS 0  # No magnetic monopoles
        ASSERT CURL(E_field) EQUALS i*omega*B_field  # Faraday's law
        ASSERT CURL(B_field) EQUALS mu_0*J - i*omega*mu_0*epsilon_0*E_field  # Ampère-Maxwell
        
        # Calculate Poynting vector (energy flow)
        # S = (1/2) * Re[Ẽ × B̃*]
        SET poynting_vector TO 0.5 * REAL(E_field CROSS CONJUGATE(B_field))
        
        # Wave impedance in the medium
        SET impedance TO sqrt(mu/epsilon) * sqrt((1 + i*sigma/(omega*epsilon)))
        SET impedance_magnitude TO |impedance|
        SET impedance_phase TO ARG(impedance)
        
        # Reflection and transmission at interfaces
        FOR EACH interface IN boundary.interfaces DO:
            SET n1 TO interface.refractive_index_1
            SET n2 TO interface.refractive_index_2
            SET theta_i TO interface.incident_angle
            
            # Snell's law in complex form for absorbing media
            SET sin_theta_t TO (n1/n2) * sin(theta_i)
            SET theta_t TO arcsin(sin_theta_t)  # May be complex for total internal reflection
            
            # Fresnel coefficients (complex for absorbing media)
            # S-polarization (TE)
            SET r_s TO (n1*cos(theta_i) - n2*cos(theta_t)) / 
                       (n1*cos(theta_i) + n2*cos(theta_t))
            SET t_s TO 2*n1*cos(theta_i) / 
                       (n1*cos(theta_i) + n2*cos(theta_t))
            
            # P-polarization (TM)
            SET r_p TO (n2*cos(theta_i) - n1*cos(theta_t)) / 
                       (n2*cos(theta_i) + n1*cos(theta_t))
            SET t_p TO 2*n1*cos(theta_i) / 
                       (n2*cos(theta_i) + n1*cos(theta_t))
            
            # Power reflection and transmission
            SET R_s TO |r_s|^2
            SET R_p TO |r_p|^2
            SET T_s TO REAL(n2*cos(theta_t)/(n1*cos(theta_i))) * |t_s|^2
            SET T_p TO REAL(n2*cos(theta_t)/(n1*cos(theta_i))) * |t_p|^2
            
            # Verify energy conservation
            ASSERT R_s + T_s EQUALS 1 WITHIN_TOLERANCE 1e-10
            ASSERT R_p + T_p EQUALS 1 WITHIN_TOLERANCE 1e-10
        END_FOR
        
        # Near-field to far-field transformation using complex Green's function
        SET far_field TO []
        # Define observation angles grid
        SET theta_range TO LINSPACE(0, pi, 180)  # Elevation angles
        SET phi_range TO LINSPACE(0, 2*pi, 360)  # Azimuth angles
        
        FOR theta IN theta_range DO:
            FOR phi IN phi_range DO:
                SET r_hat TO [sin(theta)*cos(phi), sin(theta)*sin(phi), cos(theta)]
                SET r TO 1000 * wavelength  # Far-field distance
                SET green_function TO e^(i*k*r) / (4*pi*r)
                
                # Radiation integral
                SET E_far TO INTEGRATE (
                    n_hat CROSS (n_hat CROSS J) * green_function
                ) OVER_SURFACE source_surface
                
                APPEND E_far TO far_field
            END_FOR
        END_FOR
        
        # Antenna radiation pattern
        SET radiation_pattern TO []
        SET max_power TO 0
        FOR EACH field_value IN far_field DO:
            SET field_magnitude TO |field_value|
            SET power_density TO field_magnitude^2 / (2*impedance_0)
            SET max_power TO MAX(max_power, power_density)
            APPEND power_density TO radiation_pattern
        END_FOR
        
        # Calculate total radiated power
        SET total_radiated_power TO INTEGRATE (
            radiation_pattern
        ) OVER solid_angle
        
        # Normalize pattern to dBi
        SET radiation_pattern_dB TO []
        FOR EACH power IN radiation_pattern DO:
            APPEND 10*log10(power/max_power) TO radiation_pattern_dB
        END_FOR
        
        RETURN {
            electric_field: E_field,
            magnetic_field: B_field,
            poynting_vector: poynting_vector,
            impedance: {magnitude: impedance_magnitude, phase: DEGREES(impedance_phase)},
            radiation_pattern_dB: radiation_pattern_dB,
            directivity: 4*pi*max_power/total_radiated_power
        }
    END_PROCEDURE

END_CONTEXT
```

#### Example: Portfolio Optimization with Complex Constraints

```
#ailang
# Markowitz Portfolio Optimization with Real-World Constraints
MATHEMATICAL_CONTEXT:
    DOMAIN: real
    PRECISION: high

    DEFINE PROCEDURE optimize_portfolio WITH PARAMETERS [returns, covariance, constraints]:
        # returns = expected returns vector
        # covariance = covariance matrix of returns
        # constraints = investment constraints
        
        SET n_assets TO LENGTH(returns)
        SET risk_free_rate TO 0.02  # 2% risk-free rate (typical treasury rate)
        
        # Define optimization problem
        OPTIMIZE:
            # Objective: Maximize Sharpe ratio
            OBJECTIVE: maximize (w'*returns - risk_free_rate) / sqrt(w'*covariance*w)
            
            # Variables
            VARIABLES: w = [w1, w2, ..., wn]  # portfolio weights
            
            # Constraints
            CONSTRAINTS:
                # Weights sum to 1
                SUM(w) = 1
                
                # Long-only constraint (no short selling)
                w >= 0
                
                # Maximum position size
                w <= constraints.max_position_size
                
                # Minimum position size (if invested)
                # Note: Non-convex constraint - solved via MIQP or heuristic if enabled
                FOR EACH wi IN w:
                    wi = 0 OR wi >= constraints.min_position_size
                END_FOR
                
                # Sector constraints
                FOR EACH sector IN constraints.sectors:
                    SUM(w[i] FOR i IN sector.assets) <= sector.max_allocation
                END_FOR
                
                # Risk constraint (Value at Risk limit)
                # VaR defined as maximum loss at confidence level (positive number)
                # Constraint: VaR should not exceed the limit
                VAR(0.95, w'*returns, w'*covariance*w) <= constraints.var_limit
                # Note: VaR(0.95) = -quantile(0.05, returns) for loss convention
                
            METHOD: sequential_quadratic_programming
        END_OPTIMIZE
        
        # Calculate portfolio metrics
        SET portfolio_return TO w'*returns
        SET portfolio_volatility TO sqrt(w'*covariance*w)
        SET sharpe_ratio TO (portfolio_return - risk_free_rate) / portfolio_volatility
        
        # Risk decomposition
        SET marginal_var TO []
        FOR i FROM 1 TO n_assets DO:
            SET marginal_contribution TO PARTIAL_DERIVATIVE(
                VAR(0.95, w'*returns, w'*covariance*w),
                w[i]
            )
            APPEND marginal_contribution TO marginal_var
        END_FOR
        
        RETURN {
            optimal_weights: w,
            expected_return: portfolio_return,
            volatility: portfolio_volatility,
            sharpe_ratio: sharpe_ratio,
            risk_contributions: marginal_var
        }
    END_PROCEDURE

END_CONTEXT
```
