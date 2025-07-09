# SECURITY.md - Security Checklist

## 🛡️ Authentication & Authorization

### Implementation Status
- [ ] **Password Hashing**: bcrypt/scrypt with proper salt rounds (min 12)
- [ ] **Session Security**: httpOnly, secure, SameSite cookies
- [ ] **JWT Security**: Strong secret, proper expiration, refresh tokens
- [ ] **Rate Limiting**: Login attempts (5/min), registration (3/min)
- [ ] **Permission Checks**: Authorization on EVERY protected endpoint
- [ ] **Password Policy**: Min length, complexity requirements

### Critical Tests
```bash
# Test unauthorized access
curl -X GET /api/user/123/profile  # Should return 401/403
curl -X GET /api/admin/users       # Should require admin role
```

---

## 📝 Input Validation & Sanitization

### Implementation Status
- [ ] **XSS Prevention**: HTML sanitization (DOMPurify, validator.js)
- [ ] **SQL Injection**: Parameterized queries, ORM usage
- [ ] **Type Validation**: Schema validation (Joi, Yup, Zod)
- [ ] **Size Limits**: Request body, file uploads, query params
- [ ] **Data Normalization**: Trim whitespace, case handling

### Critical Tests
```javascript
// Test in all input fields
<script>alert('XSS')</script>
'; DROP TABLE users; --
../../../etc/passwd
```

---

## 🚨 Secure Error Handling

### Implementation Status
- [ ] **Generic Error Messages**: No sensitive data in responses
- [ ] **Proper HTTP Status Codes**: 400, 401, 403, 404, 500
- [ ] **Logging**: Security events logged (failed logins, etc.)
- [ ] **Stack Traces**: Hidden in production environment

### Good Practice
```javascript
// ❌ BAD - Reveals system info
catch(error) { 
  res.json({error: error.message, stack: error.stack}) 
}

// ✅ GOOD - Generic message
catch(error) { 
  logger.error(error); // Log details server-side
  res.status(500).json({error: "Internal server error"}) 
}
```

---

## ⚙️ Secure Configuration

### Implementation Status
- [ ] **Security Headers**: helmet.js configured (CSP, HSTS, etc.)
- [ ] **Server Identity**: X-Powered-By header disabled
- [ ] **HTTPS Enforced**: All traffic redirected to HTTPS
- [ ] **Environment Variables**: Secrets not hardcoded
- [ ] **CORS Configuration**: Restricted origins in production
- [ ] **Dependency Updates**: Regular security patches

### Essential Headers
```javascript
app.use(helmet({
  contentSecurityPolicy: true,
  hsts: { maxAge: 31536000 },
  noSniff: true,
  xssFilter: true
}));
```

---

## 📁 File Upload Security

### Implementation Status
- [ ] **File Type Validation**: Magic bytes check, not just extension
- [ ] **Size Limits**: Maximum file size enforced
- [ ] **Metadata Stripping**: Remove EXIF/metadata automatically
- [ ] **Storage Isolation**: Files stored outside webroot
- [ ] **Virus Scanning**: For high-risk applications
- [ ] **Content Serving**: Separate domain/CDN with forced Content-Type

### Security Pipeline
```javascript
// 1. Validate type (magic bytes)
const isValidImage = checkMagicBytes(file);

// 2. Strip metadata & re-encode
const cleanFile = await sharp(file)
  .withMetadata(false)
  .jpeg()
  .toBuffer();

// 3. Store in isolated location
await storeFile(cleanFile, isolatedPath);
```

---

## 🔍 Security Testing Checklist

### Before Each Release
- [ ] Run security scanner (OWASP ZAP, npm audit)
- [ ] Test with malicious inputs (XSS, SQLi payloads)
- [ ] Verify authentication bypasses
- [ ] Check for information disclosure
- [ ] Test file upload restrictions
- [ ] Validate rate limiting effectiveness

### Common Attack Vectors to Test
```bash
# Authentication bypass
- Direct object references (/api/user/1, /api/user/2)
- Missing authorization checks
- Session fixation/hijacking

# Input attacks  
- XSS in all form fields
- SQL injection in search/filters
- Path traversal in file operations
- Command injection in system calls

# Configuration issues
- Debug mode enabled
- Default credentials
- Exposed sensitive endpoints
```

---

## 📚 Security Resources

### Tools
- **Static Analysis**: ESLint security plugins, Semgrep
- **Dependency Scanning**: npm audit, Snyk
- **Runtime Protection**: helmet.js, express-rate-limit
- **Testing**: OWASP ZAP, Burp Suite Community

### Learning
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security)
- [Node.js Security Checklist](https://nodejs.org/en/docs/guides/security/)

---

## 📝 Notes & Custom Threats

<!-- Add project-specific security considerations here -->

### Project-Specific Risks
- [ ] Custom risk 1: [Description]
- [ ] Custom risk 2: [Description]

### Security Incidents Log
- **Date**: Incident description and resolution

---

*Last updated: [Date]*
*Security review by: [Name]*