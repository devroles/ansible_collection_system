import hudson.security.csrf.DefaultCrumbIssuer;
import jenkins.model.Jenkins;

def jenkins = Jenkins.instance;
if( jenkins.getCrumbIssuer == null ) {
	jenkins.setCrumbIssuer(new DefaultCrumbIssuer(true));
	jenkins.save();
	println "CHANGED: Created new issuer"
}
