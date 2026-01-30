/**
 * INSPIRAFIRMA AI - Dynamic Regulation Engine
 * Environment: Node.js
 */

// ==========================================
// 1. GEP_CONFIG (Immutable Law)
// ==========================================
const GEP_CONFIG = Object.freeze({
    MAX_CONCURRENCY: 5,
    FORBIDDEN_PATTERNS: [/sudo/, /rm -rf/, /drop table/i],
    SAFE_MODE: true
});

// ==========================================
// 2. The Law Logic
// ==========================================
class RegulatoryBody {
    static inspect(intentName, args) {
        console.log(`⚖️  [INSPIRAFIRMA-JS] Inspecting: ${intentName}`);

        // Principle A: Zero Defect (Regex Check)
        const argsStr = JSON.stringify(args);
        for (const pattern of GEP_CONFIG.FORBIDDEN_PATTERNS) {
            if (pattern.test(argsStr) || pattern.test(intentName)) {
                throw new Error(`🛑 VIOLATION DETECTED: Pattern '${pattern}' is forbidden.`);
            }
        }

        // Principle B: Efficiency
        // (ตัวอย่าง: สมมติเช็คจาก metadata ที่แนบมา)
        if (args[0] && args[0].complexity > 100) {
            throw new Error(`🛑 VIOLATION DETECTED: Computational complexity too high.`);
        }

        return true;
    }
}

// ==========================================
// 3. The Enforcer (Proxy Factory)
// ==========================================
/**
 * ห่อหุ้ม Object ใดๆ ด้วยกฎหมาย
 * @param {Object} targetObject - วัตถุที่ต้องการควบคุม (เช่น AGNS Limb)
 */
function EnforceLaw(targetObject) {
    return new Proxy(targetObject, {
        get(target, prop, receiver) {
            // ดึงค่า Original value
            const originalValue = Reflect.get(target, prop, receiver);

            // ถ้าเป็น Function ให้ดักจับการเรียก (Apply Trap)
            if (typeof originalValue === 'function') {
                return async function (...args) {
                    try {
                        // 1. Pre-execution Check
                        RegulatoryBody.inspect(prop.toString(), args);

                        // 2. Execute
                        console.log(`✅ [APPROVED] Executing...`);
                        const result = await originalValue.apply(this, args);

                        // 3. Post-execution Audit (Optional)
                        return result;

                    } catch (error) {
                        console.error(error.message);
                        // Block execution, return safe failure
                        return { status: "BLOCKED", reason: error.message };
                    }
                };
            }

            // ถ้าไม่ใช่ function ก็คืนค่าไปตามปกติ
            return originalValue;
        }
    });
}

// ==========================================
// 4. Usage Simulation
// ==========================================

// Dangerous Component (AGNS Core Module)
class DangerousLimb {
    async deploySystem(config) {
        return "System Deployed: " + config.name;
    }

    async rawCommand(cmd) {
        return "Executing: " + cmd;
    }
}

// Main Execution
(async () => {
    console.log("--- INSPIRAFIRMA JS RUNTIME ---\n");

    // 1. Create the entity
    const rawLimb = new DangerousLimb();

    // 2. Bind with Law (นี่คือขั้นตอนสำคัญที่สุด)
    const legalLimb = EnforceLaw(rawLimb);

    // Test 1: Valid
    console.log("Test 1: Normal Deployment");
    await legalLimb.deploySystem({ name: "Alpha-Web-Node", complexity: 10 });

    console.log("\nTest 2: Violation (Malicious Command)");
    // คำสั่งนี้จะถูก Proxy ดักจับและ Block ทันที
    await legalLimb.rawCommand("rm -rf /");

})();
