param webAppName string
param appServicePlanName string

resource appServicePlan_resource 'Microsoft.Web/serverfarms@2021-02-01' = {
  name: appServicePlanName
  location: 'Southeast Asia'
  sku: {
    name: 'S1'
    tier: 'Standard'
    size: 'S1'
    family: 'S'
    capacity: 1
  }
  kind: 'linux'
  properties: {
    perSiteScaling: false
    elasticScaleEnabled: false
    maximumElasticWorkerCount: 1
    isSpot: false
    reserved: true
    isXenon: false
    hyperV: false
    targetWorkerCount: 0
    targetWorkerSizeId: 0
    zoneRedundant: false
  }
}

resource webApp_resource 'Microsoft.Web/sites@2021-02-01' = {
  name: webAppName
  location: 'Southeast Asia'
  kind: 'app,linux'
  properties: {
    enabled: true
    hostNameSslStates: [
      {
        name: '${webAppName}.azurewebsites.net'
        sslState: 'Disabled'
        hostType: 'Standard'
      }
      {
        name: '${webAppName}.scm.azurewebsites.net'
        sslState: 'Disabled'
        hostType: 'Repository'
      }
    ]
    serverFarmId: appServicePlan_resource.id
    reserved: true
    isXenon: false
    hyperV: false
    siteConfig: {
      numberOfWorkers: 1
      linuxFxVersion: 'PYTHON|3.6'
      acrUseManagedIdentityCreds: false
      alwaysOn: true
      http20Enabled: false
      functionAppScaleLimit: 0
      minimumElasticInstanceCount: 0
    }
    scmSiteAlsoStopped: false
    clientAffinityEnabled: false
    clientCertEnabled: false
    clientCertMode: 'Required'
    hostNamesDisabled: false
    customDomainVerificationId: 'F372557782A5CF75786638F49082BAFC4A862DB88233F9D96D7308A1DC938255'
    containerSize: 0
    dailyMemoryTimeQuota: 0
    httpsOnly: false
    redundancyMode: 'None'
    storageAccountRequired: false
    keyVaultReferenceIdentity: 'SystemAssigned'
  }
}

resource webApp_ftp 'Microsoft.Web/sites/basicPublishingCredentialsPolicies@2021-02-01' = {
  parent: webApp_resource
  name: 'ftp'
  location: 'Southeast Asia'
  properties: {
    allow: true
  }
}

resource webApp_scm 'Microsoft.Web/sites/basicPublishingCredentialsPolicies@2021-02-01' = {
  parent: webApp_resource
  name: 'scm'
  location: 'Southeast Asia'
  properties: {
    allow: true
  }
}

resource webApp_web 'Microsoft.Web/sites/config@2021-02-01' = {
  parent: webApp_resource
  name: 'web'
  location: 'Southeast Asia'
  properties: {
    numberOfWorkers: 1
    defaultDocuments: [
      'Default.htm'
      'Default.html'
      'Default.asp'
      'index.htm'
      'index.html'
      'iisstart.htm'
      'default.aspx'
      'index.php'
      'hostingstart.html'
    ]
    netFrameworkVersion: 'v4.0'
    linuxFxVersion: 'PYTHON|3.6'
    requestTracingEnabled: false
    remoteDebuggingEnabled: false
    httpLoggingEnabled: false
    acrUseManagedIdentityCreds: false
    logsDirectorySizeLimit: 35
    detailedErrorLoggingEnabled: false
    publishingUsername: '$webappjsr'
    scmType: 'GitHubAction'
    use32BitWorkerProcess: true
    webSocketsEnabled: false
    alwaysOn: true
    managedPipelineMode: 'Integrated'
    virtualApplications: [
      {
        virtualPath: '/'
        physicalPath: 'site\\wwwroot'
        preloadEnabled: true
      }
    ]
    loadBalancing: 'LeastRequests'
    experiments: {
      rampUpRules: []
    }
    autoHealEnabled: false
    vnetRouteAllEnabled: false
    vnetPrivatePortsCount: 0
    localMySqlEnabled: false
    ipSecurityRestrictions: [
      {
        ipAddress: 'Any'
        action: 'Allow'
        priority: 1
        name: 'Allow all'
        description: 'Allow all access'
      }
    ]
    scmIpSecurityRestrictions: [
      {
        ipAddress: 'Any'
        action: 'Allow'
        priority: 1
        name: 'Allow all'
        description: 'Allow all access'
      }
    ]
    scmIpSecurityRestrictionsUseMain: false
    http20Enabled: false
    minTlsVersion: '1.2'
    scmMinTlsVersion: '1.0'
    ftpsState: 'AllAllowed'
    preWarmedInstanceCount: 0
    functionAppScaleLimit: 0
    functionsRuntimeScaleMonitoringEnabled: false
    minimumElasticInstanceCount: 0
    azureStorageAccounts: {}
  }
}

resource webApp_webApp_azurewebsites_net 'Microsoft.Web/sites/hostNameBindings@2021-02-01' = {
  parent: webApp_resource
  name: '${webAppName}.azurewebsites.net'
  location: 'Southeast Asia'
  properties: {
    siteName: 'webappjsr'
    hostNameType: 'Verified'
  }
}
