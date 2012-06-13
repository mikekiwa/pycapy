#!/usr/bin/python

#This module simply defines the specific protocols possible in specified fields of an IP packet.

import struct

#This list taken from http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xml

protoList = {	"HOPOPT" 			: 	'\x00',
				"ICMP"				:	'\x01',
				"IGMP"				:	'\x02',
				"GGP"				:	'\x03',
				"IPv4"				:	'\x04',
				"ST"				:	'\x05',
				"TCP"				:	'\x06',
				"CBT"				:	'\x07',
				"EGP"				:	'\x08',
				"IGP"				:	'\x09',
				"BBN-RCC-MON"		:	'\x0a',
				"NVP-II"			:	'\x0b',
				"PUP"				:	'\x0c',
				"ARGUS"				:	'\x0d',
				"EMCON"				:	'\x0e',
				"XNET"				:	'\x0f',
				"CHAOS"				:	'\x10',
				"UDP"				:	'\x11',
				"MUX"				:	'\x12',
				"DCN-MEAS"			:	'\x13',
				"HMP"				:	'\x14',
				"PRM"				:	'\x15',
				"XNS-IDP"			:	'\x16',
				"TRUNK-1"			:	'\x17',
				"TRUNK-2"			:	'\x18',
				"LEAF-1"			:	'\x19',
				"LEAF-2"			:	'\x1a',
				"RDP"				:	'\x1b',
				"IRTP"				:	'\x1c',
				"ISO-TP4"			:	'\x1d',
				"NETBLT"			:	'\x1e',
				"MFE-NSP"			:	'\x1f',
				"MERIT-INP"			:	'\x20',
				"DCCP"				:	'\x21',
				"3PC"				:	'\x22',
				"IDPR"				:	'\x23',
				"XTP"				:	'\x24',
				"DDP"				:	'\x25',
				"IDPR-CMTP"			:	'\x26',
				"TP++"				:	'\x27',
				"IL"				:	'\x28',
				"IPv6"				:	'\x29',
				"SDRP"				:	'\x2a',
				"IPv6-Frag"			:	'\x2b',
				"IDRP"				:	'\x2c',
				"RSVP"				:	'\x2d',
				"GRE"				:	'\x2e',
				"DSR"				:	'\x2f',
				"BNA"				:	'\x30',
				"ESP"				:	'\x31',
				"AH"				:	'\x32',
				"I-NLSP"			:	'\x33',
				"SWIPE"				:	'\x34',
				"NARP"				:	'\x35',
				"MOBILE"			:	'\x36',
				"TLSP"				:	'\x37',
				"SKIP"				:	'\x38',
				"IPv6-ICMP"			:	'\x39',
				"IPv6-NoNxt"		:	'\x3a',
				"IPv6-Opts"			:	'\x3b',
				"ANY_IN"			:	'\x3c',
				"CFTP"				:	'\x3d',
				"ANY-LOCAL"			:	'\x3e',
				"SAT-EXPAK"			:	'\x3f',
				"KRYPTOLAN"			:	'\x40',
				"RVD"				:	'\x41',
				"IPPC"				:	'\x42',
				"DIST-FILE"			:	'\x43',
				"SAT-MON"			:	'\x44',
				"VISA"				:	'\x45',
				"IPCV"				:	'\x46',
				"CPNX"				:	'\x47',
				"CPHB"				:	'\x48',
				"WSN"				:	'\x49',
				"PVP"				:	'\x4a',
				"BR-SAT-MON"		:	'\x4b',
				"SUN-ND"			:	'\x4c',
				"WB-MON"			:	'\x4d',
				"WB-EXPAK"			:	'\x4e',
				"ISO-IP"			:	'\x4f',
				"VMTP"				:	'\x50',
				"SECURE-VMTP"		:	'\x51',
				"VINES"				:	'\x52',
				"TTP"				:	'\x53',
				"IPTM"				:	'\x54',
				"NSFNET-IGP"		:	'\x55',
				"DGP"				:	'\x56',
				"TCF"				:	'\x57',
				"EIGRP"				:	'\x58',
				"OSPFIGP"			:	'\x59',
				"Sprite-RPC"		:	'\x5a',
				"LARP"				:	'\x5b',
				"MTP"				:	'\x5c',
				"AX.25"				:	'\x5d',
				"IPIP"				:	'\x5e',
				"MICP"				:	'\x5f',
				"SCC-SP"			:	'\x60',
				"ETHERIP"			:	'\x61',
				"ENCAP"				:	'\x62',
				"PRIV-ENCRYP"		:	'\x63',
				"GMTP"				:	'\x64',
				"IFMP"				:	'\x65',
				"PNNI"				:	'\x66',
				"PIM"				:	'\x67',
				"ARIS"				:	'\x68',
				"SCPS"				:	'\x69',
				"QNX"				:	'\x6a',
				"A/N"				:	'\x6b',
				"IPComp"			:	'\x6c',
				"SNP"				:	'\x6d',
				"Compaq-Peer"		:	'\x6e',
				"IPX-in-IP"			:	'\x6f',
				"VRRP"				:	'\x70',
				"PGM"				:	'\x71',
				"ANY-0-HOP"			:	'\x72',
				"L2TP"				:	'\x73',
				"DDX"				:	'\x74',
				"IATP"				:	'\x75',
				"STP"				:	'\x76',
				"SRP"				:	'\x77',
				"UTI"				:	'\x78',
				"SMP"				:	'\x79',
				"SM"				:	'\x7a',
				"PTP"				:	'\x7b',
				"ISIS-OVER-IPv4"	:	'\x7c',
				"FIRE"				:	'\x7d',
				"CRTP"				:	'\x7e',
				"CRUDP"				:	'\x7f',
				"SSCOPMCE"			:	'\x80',
				"IPLT"				:	'\x81',
				"SPS"				:	'\x82',
				"PIPE"				:	'\x83',
				"SCTP"				:	'\x84',
				"FC"				:	'\x85',
				"RSVP-E2E-IGNORE"	:	'\x86',
				"MOBILE-HEADER"		:	'\x87',
				"UDPLITE"			:	'\x88',
				"MPLS-in-IP"		:	'\x89',
				"MANET"				:	'\x8a',
				"HIP"				:	'\x8b',
				"SHIM6"				:	'\x8c',
				"WESP"				:	'\x8d',
				"ROHC"				:	'\x8e',
				"EXPERIMENT"		:	'\xfd',
				"EXPERIMENT"		:	'\xfe'
			}

#Using list comprehension to easily manage this.
def getProto( value ):
	if ( len(value) > 1 ) : print "Protocol Requires One Byte (e.g. '\\x06')"; exit(1)
	result = [proto for proto, v in protoList.iteritems() if v == value]
	if ( len( result ) == 0 and struct.unpack("B",value)[0] > 142 and struct.unpack("B",value)[0] < 253): result = ["RESERVED"]
	elif (result == ""):  result = ["UNKNOWN"]
	return result[0]